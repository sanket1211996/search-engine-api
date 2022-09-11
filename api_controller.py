import uvicorn
from fastapi import FastAPI
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
import search_service
import pandas as pd
from starlette.requests import Request
from starlette.responses import Response

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


async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception:
        print('Error: My Original Internal server error')
        return Response("My Original Internal server error", status_code=505)


app.middleware('http')(catch_exceptions_middleware)


@app.get("/apiv1/search-api")
async def search_api(search_text):
    sservice = search_service.SearchService()
    return sservice.filterData(search_text)



def setup():
    print('welcome to search engine api')
    uvicorn.run(app, host="127.0.0.1", port=4600)



if __name__ == '__main__':
    from os.path import exists

    file_exists = exists('./data/mini_pickle')
    if not file_exists:
        print('Making pickle')
        file_exists = exists('./data/mini.csv')
        if file_exists:
            print('CSV File found')
            df = pd.read_csv('./data/mini.csv', dtype=str)
            df.fillna("_", inplace=True)
            df['text'] = df['security_id'] + ' ' + df['cusip'] + ' ' + df['sedol'] + ' ' + df['isin'] + ' ' + df['ric'] + ' ' + \
                         df['bloomberg'] + ' ' + df['bbg'] + ' ' + df['symbol'] + ' ' + df['root_symbol'] + ' ' + df[
                             'bb_yellow'] + ' ' + df['spn']
            df.to_pickle("./data/mini_pickle")
            print('Pickle Ready')
        else:
            print('CSV File not found')
    else:
        print('Pickle Present')
    setup()