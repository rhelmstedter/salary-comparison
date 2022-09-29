
MONTHLY_PREMIUMS: dict[str, int] = {
    "CVUSD": 160,
    "FUSD": 300,
    "HESD": 0,
    "MUSD": 125,
    "OPUSD": 400,
    "OSD": 130,
    "OUHSD": 180,
    "OVSD": 350,
    "PVSD": 200,
    "RSD": 200,
    "SPUSD": 250,
    "SVUSD": 250,
    "VUSD": 0,
}

DISTRICTS: list[str] = sorted(MONTHLY_PREMIUMS.keys())

if __name__ == "__main__":
    print(type(DISTRICTS))
