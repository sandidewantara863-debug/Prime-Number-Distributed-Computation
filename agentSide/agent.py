import sys
import argparse

def is_prime(n: int) -> bool:
    print("Melihat apakah bilangan ", n, " adalah bilangan prima?")

def primes_in_range(a: int, b: int):
    print("Pencari bilangan prima dari angka ", a, "sampai dengan", b)

def parse_args():
    p = argparse.ArgumentParser(description="Aplikasi mencari bilangan prima")
    grp = p.add_mutually_exclusive_group(required=True)
    grp.add_argument("--check", type=int, help="Periksa apakah N prima")
    grp.add_argument("--range", type=int, nargs=2, metavar=('A','B'), help="Daftar prima dalam rentang A B")
    return p.parse_args()

def main():
    args = parse_args()
    if args.check is not None:
        n = args.check
        print("prima" if is_prime(n) else "bukan prima")
    elif args.range is not None:
        a, b = args.range
        if a > b:
            a, b = b, a
        primes_in_range(a, b)

if __name__ == "__main__":
    main()