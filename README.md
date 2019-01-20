# Setup
```bash
$ pwd
  -> buidle-chain
$ cd docker/base
$ docker-compose build
$ cd ..
$ docker-compose build
$ docker-compose up
```

# Send Transaction
```
$ pwd
  -> buidle-chain
$ python -m scripts.send 100 MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxnrb17FTtrgfg33ADcbcb2D7mGX+sBIn6jE24ADNKbAvqRuhonnBJxG5W21xMyfP43P4JS8Kb/e6MsdS0D5cwnvRmsgYZdCL9CvzMJ7gYGpaQ174S3ocdTveYVaMnnZExh8OCvfdGFs5O+wdBJF11jhUmKaNAS45LWjYjou3db5oJdd87ISEHOmyB1UOp4bSIvF0EI5zHMS/kXE53t2W95PdsiXStj0HpzBp0C3jwzVLGDuyvALeC6ACg+9R6exBut8mjoDgL47m3/irFy0E2XEhmmRlpxH/hvFkGVvjMIEXBwdc+p1FDNQtGXEUkCWaBiQxNE+TE02qXlsQi6S+IwIDAQAB
$ python -m scripts.send {{amount}} {{recipient_public_key}}
```
