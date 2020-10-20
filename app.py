from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title='Optimal AirBnB Pricing',
    docs_url='/'      #  Places docs at the root `/`
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

def create_app():
    """Create and configure an instance of the FastAPI application"""
    app = FastAPI(()


    @app.get('/')
    def home():
        return {'hello': 'world'}

    
    if __name__ == "__main__":
        enable_cloud_notebook()  # can run from a notebook
        uvicorn.run(app)
