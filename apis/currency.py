import requests

def main():
    base = input("First Currency:").upper()
    other = input("Second Currency:").upper()

    payload = {"base": base}
    res = requests.get("https://api.exchangeratesapi.io/latest", params=payload)

    if res.status_code != 200:
        raise Exception("Error: API request unsuccessful.")

    data = res.json()
    rate = data["rates"][other]
    print(f"1 {base} is equal to {rate} {other}")

if __name__ == "__main__":
    main()
