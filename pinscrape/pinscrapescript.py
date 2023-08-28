from pins.pinscrape import scraper

from argparse import ArgumentParser

def main():
    argsproc = ArgumentParser(
        description="a script to download files from pinterest"
    )
    argsproc.add_argument('-l', '--limit', required=True, type=int)
    argsproc.add_argument('-k', '--key', required=True)
    argsproc.add_argument('-o', '--out', dest='out', default='.')
    args = argsproc.parse_args()
    details = scraper.scrape(
        key=args.key,
        output_folder=args.out,
        max_images=int(args.limit) # otherwise it WILL fail, must be an int
    )
    if details['isDownloaded']:
        print(f"{details['url_list']}")
    
if __name__ == "__main__":
    main()