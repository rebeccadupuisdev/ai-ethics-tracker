import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from views import home_view

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def configure_routing():
    app.include_router(home_view.router)


def main():
    configure_routing()
    uvicorn.run(app)


if __name__ == "__main__":
    main()
else:
    configure_routing()
