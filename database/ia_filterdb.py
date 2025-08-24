import os
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import DuplicateKeyError
from typing import List, Dict, Any, Optional

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
        """Save media to database"""
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
        """Find one media by file_id"""
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
        """Find multiple media documents"""
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
        """Count documents in collection"""
        if query is None:
            query = {}
        return await col.count_documents(query)
    
    @classmethod
    async def delete_many(cls, query: Dict[str, Any]):
        """Delete multiple documents"""
        result = await col.delete_many(query)
        return result.deleted_count

# Additional utility functions that might be needed
async def get_search_results(query: str, file_type: str = None, max_results: int = 50, offset: int = 0):
    """Search for files by name"""
    pipeline = []
    
    # Create search filter
    search_filter = {'file_name': {'$regex': query, '$options': 'i'}}
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

# Create indexes for better performance
async def create_indexes():
    """Create database indexes"""
    try:
        await col.create_index('file_name')
        await col.create_index('file_type')
        await col.create_index([('file_name', 'text')])
        print("Database indexes created successfully")
    except Exception as e:
        print(f"Error creating indexes: {e}")

# Run index creation when module is imported
asyncio.create_task(create_indexes()) if asyncio._get_running_loop() else None
