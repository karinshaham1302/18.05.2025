from customer import Customer

def main():
    c1 = Customer("Alice", "alice@example.com", 101)
    c2 = Customer("Bob", "bob@example.com", 202)

    print(c1)
    print(repr(c2))

    c1.id = -5

if __name__ == "__main__":
    main()



