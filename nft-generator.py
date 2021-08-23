from PIL import Image
import random
import json
from model import cpu_data
from model import psu_data
from model import ram_data
from model import driver_data
from model import gpu_data
from model import case_data

TOTAL_NFT_COUNT = 10000

DATA_DIR = "data"
JSON_DIR = "json"
IMAGE_DIR = "images"

def choose_by_rarity(data):
    return random.choices(data, [item['amount'] for item in data])

def generate_nfts():
    for i in range(0, TOTAL_NFT_COUNT):
        print(f"generating {i + 1}th NFT...")
        case = choose_by_rarity(case_data)[0]
        cpu = choose_by_rarity(cpu_data)[0]
        psu = choose_by_rarity(psu_data)[0]
        ram = choose_by_rarity(ram_data)[0]
        driver = choose_by_rarity(driver_data)[0]
        gpu = choose_by_rarity(gpu_data)[0]
        image = generate_nft(case, cpu, psu, ram, driver, gpu)
        json_data = {
            "case": { "size": case["size"], "rarity": case["rarity"] },
            "cpu": { "cpu": cpu["cpu"], "model": cpu["model"], "rarity": cpu["rarity"] },
            "psu": { "watt": psu["watt"], "rarity": psu["rarity"] },
            "ram": { "size": ram["size"], "speed": ram["speed"], "rarity": ram["rarity"] },
            "drive": { "type": driver["type"], "rarity": driver["rarity"] },
            "gpu": { "model": gpu["model"], "rarity": gpu["rarity"] },
        }
        # save image
        image_path = f"{DATA_DIR}/{IMAGE_DIR}/{i + 1}.png"
        image.save(image_path)
        # save json
        json_path = f"{DATA_DIR}/{JSON_DIR}/{i + 1}.json"
        json_str = json.dumps(json_data, indent=2)
        f = open(json_path, "w")
        f.write(json_str)
        f.close()
    print("finished generating all NFTs.")


def generate_nft(case, cpu, psu, ram, driver, gpu):
    case = Image.open(f"assets/CASE/{case['imageName']}")
    cpu = Image.open(f"assets/CPU/{cpu['imageName']}")
    psu = Image.open(f"assets/PSU/{psu['imageName']}")
    ram = Image.open(f"assets/RAM/{ram['imageName']}")
    driver = Image.open(f"assets/DRIVE/{driver['imageName']}")
    gpu = Image.open(f"assets/GPU/{gpu['imageName']}")

    case.paste(cpu, (0, 0), cpu)
    case.paste(psu, (0, 0), psu)
    case.paste(ram, (0, 0), ram)
    case.paste(gpu, (0, 0), gpu)
    case.paste(driver, (0, 0), driver)
    
    return case

if __name__ == '__main__':
    generate_nfts()
