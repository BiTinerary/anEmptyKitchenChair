<img src='https://github.com/BiTinerary/anEmptyKitchenChair/blob/master/Graveyard/Cemetery.png'>

# anEmptyKitchenChair
Context sheds light on Truth. Without it, your perspective is in the dark. In honor of the unjustly departed.

### What?
Use The Gaurdian's and Washington Posts databases of police involved deaths and shooting deaths, respectively, to download and organize 'eye witness' perspective which body cams, dash cams and cell phone footage provide. Along with news article .htmls, official police reports .pdfs, etc...  
  
Folder/file structure example:
<img src='https://github.com/BiTinerary/anEmptyKitchenChair/blob/master/Graveyard/treeExample.png?raw=true'>

### How?
Automate Google searches for each of the deceased names + "Police Shooting" and collect the top three results. If a link is to youtube, download the video. Else, download the html/pdfs file. Note that API results do vary from manual search results.

**Reaper.py** == for each name in json, do google search + "police shooting". Gather first 3 results. Add links to json.  
**Gravedigger.py** == youtube-dl/wget the aquired links/urls and store them offline in a file of the deceased.  
**Ghosts.py** == Some google searches didn't return results or errored out for various reasons. Make sure they are counted.  
**deathRattle.py** == Check WAPO dbase every hour. If new entry, send SMS with name, race, age, COD, etc... Notification for any message received by Twilio phone # is the sound of a 9MM being fired.

Automation/offline content allows for:
* Updating dbase info as more content comes out and trials/lawsuits/prosecutions are finalized.
* Automating parts of the manual process involved in updating databases with more info.
* Prevention of dead links, unavailable content and potential censorship.
* Easier to navigate than clicking and searching for each piece of relevant data.
* Machine Learning analysis? ie: Officer aquitted or charged?

### Why?

Do I need more of a reason than an enlightened perspective and pursuance of accountability?  
**O**bsession t**o** **o**bserve **a**n **o**bjectively **o**bvious **o**ppression **o**f **l**ife **a**nd **l**iberty **l**eaves **o**nly **l**amenting **o**utrage.

Victim, criminal, servant or otherwise. This is in dedication of everyone **affected** by the loss of life represented by each headstone above. You've kept me awake at night.

### Inaccuracies
Think about it, not all search results provide you with the exact content you're looking for. As such, some links are for unrelated material. For instance, common names + Police shootings might return a result for a different person (not killed by police) involved in a completely different set of circumstances. Additionally, if the case doesn't have an online presence, some links have been known to go to a wikipedia page for someone completely irrelevant. Keep these facts in mind. This is why three results are returned but the innaccuracies are well worth the projects over all accuracy and effectiveness. More will be done later on to correct inaccurate results, manually.
