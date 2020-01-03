import argparse as ap
import re
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def get_args():
    p = ap.ArgumentParser()
    p.add_argument("--url1", type=str, required=True, help="This is the starting url")
    p.add_argument("--url2", type=str, required=True, help="This is the ending url")
    return p.parse_args()

def get_links(driver):
    elems = driver.find_elements_by_xpath("//a[@href]")
    return elems

def iterative_bfs(driver, target):
    path = {}
    queue = [driver.current_url]
    while queue:
        try:
            driver.get(queue[0])
            queue.pop(0)
            elems = get_links(driver)
            for elem in elems:
                if re.match("https://en.wikipedia.org/wiki/*", elem.get_attribute("href")):
                    if elem.get_attribute("href") == target:
                        path[elem.get_attribute("href")] = driver.current_url
                        return path
                    elif elem.get_attribute("href") not in path:
                        path[elem.get_attribute("href")] = driver.current_url
                        queue.append(elem.get_attribute("href"))
        except:
            print("Element does not exist anymore")

def print_path(path, url1, url2):
    order = [url2]
    while order[-1] != url1:
        order.append(path[order[-1]])
    order.reverse()
    for elem in order:
        print(elem)

def main():
    args = get_args()
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    driver.get(args.url1)
    path = iterative_bfs(driver, args.url2)
    print_path(path, args.url1, args.url2)
    
if __name__ == "__main__":
    main()
