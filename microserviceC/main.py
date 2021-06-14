from app import create_app
from app.kafka.consumer import consume
import threading

app = create_app()
def run():
    app.run("0.0.0.0",8001)


if __name__ == '__main__':
    t = threading.Thread(target=consume)

    t.start()
    run()
    
    
