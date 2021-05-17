KEYWORDS = ["dev", "backup", "develop", "int", "internal", "staging", "test"]
with open("../../roots.txt") as roots:
    with open("targets.txt", "w+") as targets:
        for domain in roots:
            for keyword in KEYWORDS:
                target = domain.strip("\n") + "-" + keyword.strip("\n") + ".oss.eu-west-1.aliyuncs.com" + "\n"
                targets.write(target)
