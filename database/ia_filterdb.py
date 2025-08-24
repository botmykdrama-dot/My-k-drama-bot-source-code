import os
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import DuplicateKeyError
from typing import List, Dict, Any, Optional
import re

# Database configuration
DATABASE_URI = os.environ.get('DATABASE_URI')
DATABASE_NAME = os.environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Telegram_files')

# Create motor client
client = AsyncIOMotorClient(DATABASE_URI)
db = client[DATABASE_NAME]
col = db[COLLECTION_NAME]

class Media:
    def __init__(self, file_id=None, file_ref=None, file_name=None, file_size=None, file_type=None, mime_type=None, caption=None):
        self.file_id = file_id
        self.file_ref = file_ref  
        self.file_name = file_name
        self.file_size = file_size
        self.file_type = file_type
        self.mime_type = mime_type
        self.caption = caption
    
    async def save(self):
        try:
            doc = {
                '_id': self.file_id,
                'file_id': self.file_id,
                'file_ref': self.file_ref,
                'file_name': self.file_name,
                'file_size': self.file_size,
                'file_type': self.file_type,
                'mime_type': self.mime_type,
                'caption': self.caption
            }
            await col.insert_one(doc)
            return True
        except DuplicateKeyError:
            return False
        except Exception as e:
            print(f"Error saving media: {e}")
            return False
    
    @classmethod
    async def find_one(cls, file_id: str):
        doc = await col.find_one({'_id': file_id})
        if doc:
            return cls(
                file_id=doc.get('file_id'),
                file_ref=doc.get('file_ref'),
                file_name=doc.get('file_name'),
                file_size=doc.get('file_size'),
                file_type=doc.get('file_type'),
                mime_type=doc.get('mime_type'),
                caption=doc.get('caption')
            )
        return None
    
    @classmethod
    async def find(cls, query: Dict[str, Any], limit: int = 50):
        cursor = col.find(query).limit(limit)
        results = []
        async for doc in cursor:
            results.append(cls(
                file_id=doc.get('file_id'),
                file_ref=doc.get('file_ref'),
                file_name=doc.get('file_name'),
                file_size=doc.get('file_size'),
                file_type=doc.get('file_type'),
                mime_type=doc.get('mime_type'),
                caption=doc.get('caption')
            ))
        return results
    
    @classmethod  
    async def count_documents(cls, query: Dict[str, Any] = None):
        if query is None:
            query = {}
        return await col.count_documents(query)
    
    @classmethod
    async def delete_many(cls, query: Dict[str, Any]):
        result = await col.delete_many(query)
        return result.deleted_count

# Search function
async def get_search_results(query: str, file_type: str = None, max_results: int = 50, offset: int = 0):
    pipeline = []
    
    # Create search filter using regex for case-insensitive search
    search_words = query.split()
    regex_pattern = '.*'.join([re.escape(word) for word in search_words])
    search_filter = {'file_name': {'$regex': regex_pattern, '$options': 'i'}}
    
    if file_type:
        search_filter['file_type'] = file_type
    
    pipeline.append({'$match': search_filter})
    pipeline.append({'$skip': offset})
    pipeline.append({'$limit': max_results})
    
    cursor = col.aggregate(pipeline)
    results = []
    
    async for doc in cursor:
        results.append(Media(
            file_id=doc.get('file_id'),
            file_ref=doc.get('file_ref'),
            file_name=doc.get('file_name'),
            file_size=doc.get('file_size'),
            file_type=doc.get('file_type'),
            mime_type=doc.get('mime_type'),
            caption=doc.get('caption')
        ))
    
    return results

# Create indexes
async def create_indexes():
    try:
        await col.create_index('file_name')
        await col.create_index('file_type')  
        await col.create_index([('file_name', 'text')])
        print("Database indexes created successfully")
    except Exception as e:
        print(f"Error creating indexes: {e}")
