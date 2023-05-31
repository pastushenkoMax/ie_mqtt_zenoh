import zenoh, random, time

random.seed()

def read_rmp():
    return random.randint(115, 120)

if __name__ == "__main__":
    session = zenoh.open()
    key = 'Heptopod-Delta-Fixture/Delta-Right/Center-Stepper-Motor'
    pub = session.declare_publisher(key)
    while True:
        t = read_rmp()
        buf = f"==== RPM: {t} ===="
        print(f"Putting Data ('{key}': '{buf}')...")
        pub.put(buf)
        time.sleep(1)