from langchain.text_splitter import RecursiveCharacterTextSplitter, Language
from langchain_community.document_loaders import PyPDFLoader
import asyncio
import random

loader = PyPDFLoader(r"datasets\dev.epicgames.com-Niagara Overview.pdf")
pages = []


async def load_pages():
    async for page in loader.alazy_load():
        pages.append(page)


asyncio.run(load_pages())
print(len(pages))


splitter = RecursiveCharacterTextSplitter(chunk_size=30, chunk_overlap=0)
chunks = splitter.split_documents(pages)
print(chunks[random.randint(0, len(chunks) - 1)].page_content)
