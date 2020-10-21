from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.api import predict, viz

"""Create and configure an instance of the FastAPI application"""
app = FastAPI(
    title='Optimal AirBnB Pricing API',
    description='An application that predicts the optimal pricing for an AirBnB',
    version='0.1',
    docs_url='/'      #  Places docs at the root `/`
)

@app.get('/')
def index():
    return {'hello': 'world'}

app.include_router(predict.router)
app.include_router(viz.router)

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex='https?://.*',
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)



def enable_cloud_notebook(port=8000):
    """
    Enables you to run a FastAPI app from a cloud notebook.
    Useful for rapid prototyping if you like notebooks!
    Not needed when you develop in a local IDE or deploy "for real."
    """

    # Prevent "RuntimeError: This event loop is already running"
    import nest_asyncio
    nest_asyncio.apply()

    # Get a public URL to the localhost server 
    from pyngrok import ngrok
    print('Public URL:', ngrok.connect(port=port))


if __name__ == '__main__':
    uvicorn.run(app)
    enable_cloud_notebook()  # can run from a notebook
