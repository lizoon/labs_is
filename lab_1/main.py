from forward_chaining_engine import ForwardChainingEngine
from kb import KnowledgeBase

if __name__ == "__main__":
    inference_engine = ForwardChainingEngine()
    knowledge_base = KnowledgeBase(inference_engine)

    facts = [
        "Class Mammal Elephant",
        "Class Mammal Lion",
        "Class Bird Eagle",
        "Class Bird Penguin",
        "Class Fish Shark",

        "Habitat Elephant Savannah",
        "Habitat Lion Savannah",
        "Habitat Eagle Mountains",
        "Habitat Penguin Antarctica",
        "Habitat Shark Ocean",

        "Eats Elephant Plants",
        "Eats Lion Meat",
        "Eats Eagle Fish",
        "Eats Penguin Fish",
        "Eats Shark Fish",
    ]

    for fact in facts:
        knowledge_base.add_fact(fact)

    # AnlimalClass, Animal, Habitat, Food
    rules = [
        "Class Mammal ?mammal & Eats ?mammal ?food => WarmBlooded ?mammal",
        "Class Bird ?bird & Habitat ?bird Mountains => CanFly ?bird",
        "Class Fish ?fish & Habitat ?fish Ocean => CanSwim ?fish",
    ]
    for rule in rules:
        knowledge_base.add_rule(rule)

    queries = [
        "Class Bird ?bird",
        "Habitat Penguin ?habitat",
        "Eats Lion ?food",
        "CanFly ?bird",
        "CanSwim Shark",
        "WarmBlooded ?mammal"
    ]

    for query in queries:
        res = knowledge_base.query(query)
        # print(res)
        if len(res) == 0:
            print("-")
        for r in res:
            print(str(r))
        print()
