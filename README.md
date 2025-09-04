# Bug Bounty Tools

Tools to make the Bug Bounty Hunter's day-to-day work easier.

## toc-toc.py

[toc-toc.py](../toc-toc.py): Tool to determine whether a domain or subdomains are active or not. This is very useful in Bug Bounties where we find a very wide scope. For example, if we use SecurityTrails or any subdomain recognition application, we may find lists of thousands of them, many of which are inactive.

The purpose of the script is to facilitate the hunter's reconnaissance work.

### Usage

The first step will be to edit the script to add the list of subdomains we want to scan. By default, activity will be monitored using the HTTPS protocol. If we want to search port 80, we will have to define it in the *url* variable.

Next, we will run **python toc-toc.py** and it will display the results on the screen, as well as create a .txt file with all the results, sorted by status code, leaving those subdomains with connection errors for last.

```
python toc-toc.py
```

##### Configuration

![alt_text](https://github.com/daparicio8383/BugBounty-Tools/blob/main/Images/config_toc-toc.png "Modify subdomains in the script")


##### Test scan.

![alt text](https://github.com/daparicio8383/BugBounty-Tools/blob/main/Images/toc-toc.png "Testing for Google subdomains.")

