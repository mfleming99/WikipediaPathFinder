# WikipediaPathFinder
Finds the shortest path between two Wikipedia articles using BFS. This script depends on (Selenium)[https://selenium.dev/]

To use this script call

`python --url1 "Your starting Wikipedia link" --url2 "Your ending Wikipedia link"`

The output will be the shortest path between the two articals. An example usage is

```
python main.py --url1 https://en.wikipedia.org/wiki/Make_a_Smellmitment --url2 https://en.wikipedia.org/wiki/Nike,_Inc.               

https://en.wikipedia.org/wiki/Make_a_Smellmitment
https://en.wikipedia.org/wiki/Wieden%2BKennedy
https://en.wikipedia.org/wiki/Nike,_Inc.
```
