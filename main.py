import multiprocessing as mp

if __name__ == "__main__":
    mp.freeze_support()
    mp.set_start_method('spawn')

    import uvicorn
    from app.main import app
    uvicorn.run(app, host="0.0.0.0", port=8000)
