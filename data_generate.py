import math
file = open("data.txt", "w")
sum_width = 10.0
for num in range(3, 6, 1):
    width_base = sum_width / num / 2.0
    width_root = 0
    width_up = 0
    height = 0
    radius = 0
    for ra1 in range(1, 8, 3):
        width_root = width_base * (10.0 - ra1) / 10.0
        width_up = width_base * (10.0 + ra1) / 10.0
        for ra2 in range(-5, 8, 4):
            height = width_base * (10.0 + ra2) / 10.0
            radius_base1 = height / (2.0*math.cos(math.atan2(height, (width_up - width_root)/2.0)) + 2.0) * 0.95
            radius_base1 = min(radius_base1, width_up / 2.0 * math.tan(math.atan2(height, (width_up - width_root)/2.0) / 2.0) * 0.95)
            radius_base2 = (width_up - width_root) / 4.0 * math.tan(math.atan2(height, (width_up - width_root)/2.0) / 2.0) * 0.95
            radius_base2 = min(radius_base1, radius_base2)
            for ra3 in range(0, 11, 5):
                for stage in range(1, 3, 1):
                    if height*stage > 4.9:
                        continue
                    if stage == 1:
                        radius = radius_base1 * ra3 / 10.0
                    else:
                        radius = radius_base2 * ra3 / 10.0
                    file.write(f"{num} {height:.2f} {width_up:.2f} {width_root:.2f} {stage} {radius:.2f} {num}_{stage}_{ra1}_{ra2}_{ra3}\n")
