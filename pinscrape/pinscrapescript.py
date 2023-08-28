from ast import Interactive
from tokenize import group
from pins.pinscrape import scraper

from argparse import ArgumentParser


def main():
    argsproc = ArgumentParser(description="a script to download files from pinterest")
    argsgroup = argsproc.add_argument_group("interactive")
    argsproc.add_argument("-l", "--limit", required=True)
    argsproc.add_argument("-k", "--key", required=True)
    argsproc.add_argument("-o", "--out", dest="out", default=".")
    argsproc.add_argument(
        "-t", "--threads", default=10, help="number of threads to use, default is 10"
    )
    args = argsproc.parse_args()

    details = scraper.scrape(
        key=args.key,
        output_folder=args.out,
        max_images=int(args.limit),
        threads=int(args.threads),
    )
    if details["isDownloaded"]:
        print(f"{len(details['url_list'])} are downloaded")
    else:
        print("failed to download, maybe due to netw. issues?")


if __name__ == "__main__":
    main()
