As I envision it, this repo will probably contain two things, NBA projects and Caltech Basketball Projects. Data access (at a basic level) should be pretty easy to get for the NBA. For Caltech data, it may be a bit harder to facilitate, but we'll look into it more.

## NBA

### NBA Stats API (play by play data, shot chart data, etc.) 

The NBA has an public stats API that has any information that you can find on the stats.nba.com website. Unfortunately, there's no official OpenAPI spec, but the public has done some pretty comprehensive [endpoint analysis](https://github.com/swar/nba_api/blob/master/docs/table_of_contents.md)

Although some use the nba\_api package on it's own (completely based on personal preference), I (Avyay) personally prefer to use the [py\_ball](https://github.com/basketballrelativity/py_ball) wrapper. The docs on the library are pretty good. 

Keep in mind that whatever you choose to use, you will need to feed in very specific request headers if you want your queries to work. These are the headers that I've used (and work as of June 21, 2022). 

```
headers = {
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8,ru;q=0.6',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Referer': 'https://stats.nba.com/teams/boxscores-traditional/',
    'x-nba-stats-origin': 'stats',
    'x-nba-stats-token': 'true'
}
```

Note that the required headers sometimes changes from season to season - if your request hangs, that's probably why. In this case, go to the NBA stats website frontend, check the outgoing requests to the API (inspect element -> requests -> XML -> refresh, should be a stats.nba.com/stats request), and check what headers the NBA Stats frontend is using. 

## Caltech Basketball

Working on an NCAA PBP Scraper / Parser.


