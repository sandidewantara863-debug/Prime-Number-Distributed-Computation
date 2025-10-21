import sys
import argparse

def is_prime(n: int) -> bool:
    if (n < 2):
        return False
    elif (n == 2):
        return True
    elif (n % 2 == 0):
        return False
    for i in range(2,n):
        if (n % i == 0):
            print("bisa dibagi bilangan: ", i)
            return False
    return True

def primes_in_range(a: int, b: int):
    print("Pencari bilangan prima dari angka ", a, "sampai dengan", b)

def parse_args():
    p = argparse.ArgumentParser(description="Aplikasi untuk mencari bilangan prima")
    grp = p.add_mutually_exclusive_group(required=True)
    grp.add_argument("--check", type=int, help="Periksa apakah N prima")
    grp.add_argument("--range", type=int, nargs=2, metavar=('A','B'), help="Daftar prima dalam rentang A B")
    return p.parse_args()

def main():
    args = parse_args()
    if args.check is not None:
        n = args.check
        if (is_prime(n)):
            print(n, " adalah bilangan prima")
        else:
            print(n, " bukan bilangan prima")

    elif args.range is not None:
        a, b = args.range
        if a > b:
            a, b = b, a
        primes_in_range(a, b)

if __name__ == "__main__":
    main()