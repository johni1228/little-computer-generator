import json

TOTAL_NFT_COUNT = 10000

DATA_DIR = "data"
JSON_DIR = "json"
NEW_JSON_DIR = "newjson"

def convert_data():
    for i in range(0, TOTAL_NFT_COUNT):
        print(f"processing {i}th file...")
        json_path = f"{DATA_DIR}/{JSON_DIR}/{i + 1}.json"
        f = open(json_path, "r")
        json_str = f.read()
        f.close()
        json_data = json.loads(json_str)

        new_json_data = {
            "attributes": [
                {
                    "trait_type": "case",
                    "value": str(json_data["case"]["size"])
                }, {
                    "trait_type": "cpu",
                    "value": str(json_data["cpu"]["cpu"])
                }, {
                    "trait_type": "psu",
                    "value": str(json_data["psu"]["watt"])
                }, {
                    "trait_type": "ram",
                    "value": str(json_data["ram"]["size"])
                }, {
                    "trait_type": "drive",
                    "value": str(json_data["drive"]["type"])
                }, {
                    "trait_type": "gpu",
                    "value": str(json_data["gpu"]["model"])
                }
            ],
            "description": "Little Computer OpenSea Creature",
            "external_url": "",
            "name": "Little Computer"
        }
        json_str = json.dumps(new_json_data, indent=2)
        json_path = f"{DATA_DIR}/{NEW_JSON_DIR}/{i + 1}.json"
        f = open(json_path, "w")
        f.write(json_str)
        f.close()

    print("finished generating all NFTs.")


if __name__ == '__main__':
    convert_data()
