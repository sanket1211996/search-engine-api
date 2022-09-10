import uvicorn
from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
import search_service

app = FastAPI()

origins = ["*"]

middleware = [Middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], )
]

app = FastAPI(middleware=middleware)


# async def catch_exceptions_middleware(request: Request, call_next):
#     try:
#         return await call_next(request)
#     except Exception:
#         return Response("Internal server error", status_code=505)


# app.middleware('http')(catch_exceptions_middleware)


@app.get("/apiv1/search-api")
async def search_api(search_text):
    sservice = search_service.SearchService()
    return sservice.filterData(search_text)



def setup():
    print('welcome to search engine api')
    uvicorn.run(app, host="127.0.0.1", port=4600)



if __name__ == '__main__':
    setup()