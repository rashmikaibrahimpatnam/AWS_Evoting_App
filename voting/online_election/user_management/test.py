import hashlib

if __name__ == '__main__':
    print(hashlib.sha256("admin123".encode("utf-8")).hexdigest())
