from apollo import (
    mythos_1b,
    Apollo,
)

cfg = mythos_1b()
model = Apollo(cfg)

total = sum(p.numel() for p in model.parameters())
print(f"Parameters: {total:,}")
