import fitparse

def inspect_fitfile(file_path):
    fitfile = fitparse.FitFile(file_path)
    record_count = 0

    for message in fitfile.get_messages():
        print(f"Message: {message.name}")
        for record in message:
            print(f"  {record.name}: {record.value}")
            record_count += 1
            if record_count >= 100:
                return

def main():
    file_path = "fit/tp-2725125.2024-07-11-02-20-15-247Z.GarminPing.AAAAAGaPQV5UumZS.fit"
    inspect_fitfile(file_path)

if __name__ == "__main__":
    main()
