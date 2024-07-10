import logging
from langchain_chroma import Chroma

def list_chroma_collections():
    logging.debug("Listing Chroma collections")
    
    # Initialize the Chroma client
    chroma_client = Chroma()
    # help(chroma_client)
    # Debugging to inspect the Chroma client object
    # print(dir(chroma_client))
    
    # Attempting to access collections through possible attributes
    # if hasattr(chroma_client, '_collection'):
    #     collections = chroma_client._collection.get()  # Assuming _collection is the correct internal attribute
        
    #     print(collections['data'])
    # else:
    #     print("The Chroma client does not have an attribute '_collection'.")
    # chroma_client.delete_collection()
    # query_results = chroma_client._collection.get(where={"field": "value"})
    print(chroma_client._collection.get("fsfwd"))

# Extract IDs from the query results
    # relevant_ids = [record["id"] for record in query_results]

# Now 'relevant_ids' contains the IDs you need!
    # print(query_results)
    logging.debug("Listing complete")
    

if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.DEBUG)


    # List all collections
    list_chroma_collections()
