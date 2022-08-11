  
  worker:
      build: 
        context: .
        dockerfile: Dockerfile
      command: celery -A EcpDemo worker -l info
      volumes:
        - .:/code
      depends_on:
        - broker

  beat:
    build: 
      context: .
      dockerfile: Dockerfile
    command: celery -A EcpDemo beat -l info
    volumes:
      - .:/code
    depends_on:
      - broker