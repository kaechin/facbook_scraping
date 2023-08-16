# Social Media Data Platform Aggregator (SMDPA) project: Facebook Data Scraping at Kristiania University College

##  Project Description

The Social Media Data Platform Aggregator (SMDPA) project aims to create an advanced tool to overcome challenges posed by limited API access on Facebook. Inspired by CrowdTangle's discontinuation, this project focuses on developing a comprehensive data collection solution for Facebook Pages managed by companies and organizations. By utilizing ethical data practices, user-friendly design, and innovative web scraping techniques, SMDPA aims to empower researchers, analysts, and decision-makers with valuable insights into content and engagement trends. This bridge between restricted API access and data needs underscores the project's significance in the field of social media research and analysis.

This research initiative was undertaken at Kristiania University College during the period spanning from May to August 2023. Notably, the project encompassed not only the domain of Facebook data scraping but also extended to the realm of Instagram scraping.

## Prerequisites
- Internet Connection
- Visual Studio Code
- Firefox
- Python 3.7+
- React 18.2.0
- Flask 2.3.2

## How to Install

- Installing from source

```
git clone https://github.com/kaechin/facbook_scraping.git
```

- Installing React

```
npm install react react-dom
```

- Installing Flask

```
pip install Flask
```

## How to start the system

- Frontend (React)

1. Move to the frontend folder

```
cd yourfolderpath/Facebook_Scraping/facebook_page_scraper/src/frontend
```

2. Start React

```
npm start
```

- Backend (Flask)

1. Move to the backend folder

```
cd yourfolderpath/Facebook_Scraping/facebook_page_scraper/src/backend
```

2. Start React

```
python .\app.py
```

## How to use the system

1. In the Scraping Facebook Data section, enter any Facebook page name in the Facebook page box.
 <img src="Facebook Scraping 1.jpg" style="margin: 15px">

2. Enter the desired Start Date in the Start Date field.
 <img src="Facebook Scraping 2.jpg" style="margin: 15px">

3. Click the Search button.
<img src="Facebook Scraping 3.jpg" style="margin: 15px">

4. Loading will be displayed while the system is scraping the Facebook page.
<img src="Facebook Scraping 5.jpg" style="margin: 15px">

5. When the scraping is finished, the message "Scrape done" is displayed.
<img src="Facebook Scraping 6.jpg" style="margin: 15px">

6. Click the DOWNLOAD PAGE CSV button.
<img src="Facebook Scraping 7.jpg" style="margin: 15px">

7. When the download is complete, the message "CSV Download Successfully!
<img src="Facebook Scraping 8.jpg" style="margin: 15px">

8. CSV file is generated in the Download of the local terminal. The picture shows a part of the data in arnold.csv.
<img src="Facebook Scraping 16.jpg" style="margin: 30px">

9. In the Filtering Facebook Data section, enter the name of the data obtained in the Scraping Facebook Data section in the Facebook page box.
<img src="Facebook Scraping 9.jpg" style="margin: 15px">

10. Enter the desired Start Date in the Start Date field.
<img src="Facebook Scraping 10.jpg" style="margin: 15px">

11. Enter the desired end date in the End Date field.
<img src="Facebook Scraping 11.jpg" style="margin: 15px">

12. @ Search box, # Enter the @ and # you wish to retrieve in the Search box.
<img src="Facebook Scraping 12.jpg" style="margin: 15px">

13. Click the Search button.
<img src="Facebook Scraping 18.jpg" style="margin: 15px">

14. When filtering is complete, the text "Hash data for Facebook page name has been extracted and saved to Facebook page name_hashtag.csv" will be displayed.
<img src="Facebook Scraping 13.jpg" style="margin: 15px">

15. Click the DOWNLOAD HASHTAG CSV button.
<img src="Facebook Scraping 14.jpg" style="margin: 15px">

16. When the download is complete, the message "CSV Downloaded Successfully!
<img src="Facebook Scraping 15.jpg" style="margin: 15px">

17. CSV file is generated in the Download of the local terminal. The picture shows part of the data in arnold_hashtag.csv.
<img src="Facebook Scraping 17.jpg" style="margin: 30px">

## Future Work

- Depending on the network conditions, it usually takes about 5 minutes to retrieve approximately 150 pieces of information. It's evident that there's room for improvement in this area for the future.

- While prioritizing privacy is crucial, it's also worth highlighting that including comments from posts in upcoming attempts could significantly enhance the quality of the collected data. This enhancement holds great potential for facilitating future research endeavors.

- The process of extracting data from Facebook's website is closely linked to how the website is structured. Thus, if Facebook decides to change the way its website is organized, our current method of collecting data might not be as effective. If such a structural change happens, it's important to handle it based on the specific situation.

- Our current operational framework utilizes Webshare's rotation proxy infrastructure. However, in scenarios where Webshare's proxy becomes less effective and Facebook cannot be accessed as intended, it becomes imperative that the system consider proxy solutions offered by alternative companies.
  
- Currently, the system operates solely on local terminals. However, plans for future implementation include enabling deployments. This deployment aspect holds the potential to facilitate widespread utilization of the system, catering to a larger user base.

## Conclusion

The Social Media Data Platform Aggregator (SMDPA) project has effectively developed sophisticated tools to address the constraints arising from restricted API access on Facebook. Consequently, the system is poised to furnish researchers, analysts, and decision-makers with invaluable insights concerning content and engagement trends, paving the way for expanded research endeavors. As this project is slated for future expansion, the forthcoming work outlined in the designated section will be executed, culminating in the establishment of a more user-friendly system.

## Reference
Rivera, Isabel. 2023. “How to Scrape Facebook.” Proxyway. March 20, 2023. https://proxyway.com/guides/how-to-scrape-facebook.
Shaikh, Sajid. 2021. “Facebook Page Scraper.” GitHub. February 2, 2021. https://github.com/shaikhsajid1111/facebook_page_scraper/tree/master.






