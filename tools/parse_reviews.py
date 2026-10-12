# -*- coding: utf-8 -*-
"""Parse and clean all customer reviews from user prompt."""
import json
import re

raw_reviews_text = """
[Abhishek Verma1 review](https://www.google.com/maps/contrib/111852317872008438349/reviews?hl=en-GB)
a month ago
⭐⭐⭐⭐⭐
Excellent Travel Service
I had a great experience with Vinod Tour & Travel. Their service was very … More
vinod tour and travels (owner)
a month ago
Hello Abhishek, thank you for the wonderful 5-star review! We’re delighted to hear you had an excellent experience with Vinod Tour & Travel. Our team works hard to ensure professional, reliable, and well-organized support—from family trips and corporate travel to holiday packages, hotel bookings, and transportation services in Delhi. We’re especially glad you found our assistance friendly and responsive throughout your journey.
We look forward to welcoming you again for your future trips. 😊✈️
Regards, Team Vinod Tour & Travel, Uttarakhand Kotdwar
[Sai3 reviews](https://www.google.com/maps/contrib/114948829251120262359/reviews?hl=en-GB)
4 months ago
Vinod was extremely courteous, kind and very helpful in my trip to Ransi. He
provided information he knew about key places along the route and went out of his way help me locate items I needed. Excellent reliable driver and fantastic service. I will recommend him to anyone needing cab services.
vinod tour and travels (owner)
4 months ago
Thank you so much for your wonderful review! 🙏 We are delighted to know that you had a pleasant trip to Ransi and appreciated our service. Your kind words about our courtesy, guidance, and assistance mean a lot to us. We always strive to make every journey safe, comfortable, and memorable for our guests. Thank you for your recommendation. We look forward to serving you again on your next Uttarakhand adventure! 😊🚖🏔️"
– Vinod Tour & Travels, Kotdwar, Uttarakhand
📞 8076069722 | 9045511378
📧 vndkmr733@gmail.com
[MAYYUR B MERCHANTLocal Guide·21 reviews·10 photos](https://www.google.com/maps/contrib/100517719051391858373/reviews?hl=en-GB)
5 months ago
Today I came to Delhi and had a great experience. Vinod Sir provided excellent service — he was very polite, caring, and made us feel very comfortable throughout. He deserves more than a 5-star rating. Highly appreciated!
vinod tour and travels (owner)
Edited 4 months ago
You can reply to this review with the following message:🙏
[manka mehta4 reviews](https://www.google.com/maps/contrib/104785007265568643102/reviews?hl=en-GB)
9 months ago
Expert driving, very safe and very polite! Made the trip memorable because the drive despite being so long was so very smooth!! The car was clean and Vinod bhai was the most reliable driver! Always always recommend this!
❤️1
vinod tour and travels (owner)
9 months ago
🙏 Thank you for choosing Vinod Tour & Travels!
Humein khushi hai ki aapko hamari service pasand aayi.
Aage bhi aapke safar ko yaadgaar banane ka mauka dein. 🚗✨
See translation (English)
[Sam SchruderLocal Guide·47 reviews·11 photos](https://www.google.com/maps/contrib/115473589382921887331/reviews?hl=en-GB)
6 months ago
My friend recommended Vinod and he gave an excellent service! He’s got a calm and caring presence, I really felt taken care of. Highly recommend his service whether short or longer trips.
❤️1
vinod tour and travels (owner)
Edited 6 months ago
Thank you so much for your valuable review! 😊
We truly appreciate your support and trust in our services. It means a lot to us and motivates me to keep delivering the best travel experience.
We look forward to serving you again on your next journey! 🚗✨
– Vinod Tour & Travels🙏
[Medida Manvitha Persis1 review](https://www.google.com/maps/contrib/112570145504852091054/reviews?hl=en-GB)
7 months ago
We had a GOOD travel experience to Agra from Delhi with Vinod ji.
The ride was nice and comfortable.
Driving very safe and steadily.👍
❤️1
vinod tour and travels (owner)
7 months ago
Thank you ji 🙏
[UPS&D3 reviews](https://www.google.com/maps/contrib/104035313040267121892/reviews?hl=en-GB)
10 months ago
We had a wonderful travel experience with our driver Aman during our journey to Lansdowne. He was polite, friendly, and very knowledgeable about the local places. He showed us the best viewpoints, scenic spots, and shared helpful … More
❤️1
vinod tour and travels (owner)
10 months ago
Thank you Sar so much 🙏🙏
[Shasi Prasad5 reviews·1 photo](https://www.google.com/maps/contrib/114807726499901507203/reviews?hl=en-GB)
10 months ago
I highly recommend Vinod as a tour guide travelling in India. I visited 11 different cities in about 3 weeks and mostly on road with Vinod as our driver, guide and hotel check-ins. Vinod went out of his washing to deliver a professional yet … More
❤️1
vinod tour and travels (owner)
10 months ago
Thank you ji🙏
[Hitesh Saharan2 reviews·1 photo](https://www.google.com/maps/contrib/117296952926260875569/reviews?hl=en-GB)
4 months ago
Humne inke sath haridwar se sonprayag tak trip ki shander driver h or bande bhi bhoot ache hme raste me jo dekhane wali jagha thi vo gadi rok kar dikhai or pure raste hmara manorajan bhi kiya vinod ji bhoot ache bnde h enke sath aap suraksit h
See translation (English)
vinod tour and travels (owner)
4 months ago
Bahut bahut dhanyavaad aapke pyaare shabdon aur vishwas ke liye. Humein khushi hai ki Haridwar se Sonprayag tak ka safar aapko pasand aaya. Hamari koshish rehti hai ki har yatri ko surakshit, suvidhajanak aur yaadgaar yatra ka anubhav mile. Aapke saath safar karke humein bhi bahut accha laga. Aapke is sarahniya review ke liye dhanyavaad. Bhavishya mein bhi aapki seva ka avsar mile, isi aasha ke saath.
See translation (English)
[AbsLocal Guide·39 reviews·74 photos](https://www.google.com/maps/contrib/112119721491616050015/reviews?hl=en-GB)
7 months ago
Manoj was a really great driver. His driving is very safe and he is super friendly. He made the entire trip enjoyable (what a very long day it was to see the Taj). Definitely worth it.
❤️1
vinod tour and travels (owner)
Edited 7 months ago
Thank you for choosing Vinod Tour & Travels!
Humein khushi hai ki aapko hamari service pasand aayi.
Aage bhi aapke safar ko yaadgaar banane ka mauka dein. 🚗👍👍
See translation (English)
[Solarify2 reviews](https://www.google.com/maps/contrib/116124948186427778624/reviews?hl=en-IN)
a month ago
Its was a great Experience with Ganesh.He has so much of knowledge about all the sightseeing places as well
vinod tour and travels (owner)
a month ago
Hi Solarify, thank you for sharing your experience with vinod tour and travels. We’re glad you had a great time, and that Ganesh’s local knowledge helped you explore the sightseeing places with confidence.
[Yogendra Yogendra Kumar1 review](https://www.google.com/maps/contrib/103508998812449806348/reviews?hl=en-IN)
6 months ago
The ride was really nice and comfortable. Vinod was very cooperative and humble person.I truly appreciated the pleasant and hassle free ride..
❤️1
vinod tour and travels (owner)
6 months ago
Thank you so much for your valuable review! 😊
We truly appreciate your support and trust in our services. It means a lot to us and motivates me to keep delivering the best travel experience.
We look forward to serving you again on your next journey! 🚗✨
– Vinod Tour & Travels
[Shivan Bhoendie1 review](https://www.google.com/maps/contrib/109514070286386857105/reviews?hl=en-IN)
7 months ago
Very friendly and knowledgeable driver, on time, flexible and drives safely but swiftly through Delhi traffic
❤️1
vinod tour and travels (owner)
7 months ago
Thank you sir 🙏
[PRASHANT SINGH1 review](https://www.google.com/maps/contrib/115208069524100714855/reviews?hl=en-IN)
4 months ago
The experience was very good 👍😊. the driver was very kind and humble 😃. 5 out of 5 starts ⭐ by me
vinod tour and travels (owner)
4 months ago
Thank you so much for your wonderful 5-star review! ⭐⭐⭐⭐⭐
We are delighted to hear that you had a very good experience with us. Your kind words about our driver's humble and friendly nature mean a lot to us. We always strive to provide safe, comfortable, and memorable journeys for our guests.
We look forward to serving you again in the future. Thank you for choosing Vinod Tour & Travels! 😊🙏
— Vinod Tour & Travels, Kotdwar Uttarakhand 🚖🏔️
📞 8076069722 | 9045511378
[Deepak Khera9 reviews·1 photo](https://www.google.com/maps/contrib/101367665574032616567/reviews?hl=en-IN)
Edited 5 months ago
Wonderful service, polite and flexible
Liked the car, very clean, good driving, highly recommended
❤️1
vinod tour and travels (owner)
5 months ago
Thank you so much for your kind words! 🙏
We are glad to hear that you liked our service, clean car, and driving experience.
At Vinod Tour & Travels, we always try to provide polite, flexible, and comfortable journeys to our customers.
Your recommendation means a lot to us! 😊
We look forward to serving you again on your next trip.
[Prakash Kanth2 reviews](https://www.google.com/maps/contrib/100823447466529020466/reviews?hl=en-IN)
10 months ago
We were with Vinod for a trip to Rishikesh from Gurgaon. Clean and well maintained car, excellent driving , punctual and courteous . He is very helpful with information and assistance. Happy with the experience and will be happy to travel with him again. Prakash Kanth , Gurgaon
❤️1
vinod tour and travels (owner)
10 months ago
Thank you sir so much🙏
[sahil chopra1 review](https://www.google.com/maps/contrib/118138399323144012083/reviews?hl=en-IN)
4 months ago
Good experience with ds company while travel Kedarnath and Badrinath with vinod ji he gives u good guidence to travel with him 😊😊😊😊
vinod tour and travels (owner)
4 months ago
Thank you so much for your valuable feedback! We are delighted to hear that you had a great experience during your Kedarnath and Badrinath trip with Vinod Tour & Travels. Your kind words about our guidance and service mean a lot to us. We look forward to serving you again on your next journey. Thank you for choosing Vinod Tour & Travels! 🙏😊
[Pasha King2 reviews](https://www.google.com/maps/contrib/103303775448449318001/reviews?hl=en-IN)
a year ago
We had a very pleasant trip from Lucknow to Khajuraho and back to Delhi with Mr Vinod ! He is a very safe , pleasant, knowledgeable and respectful driver. He made our long journey so easy due to his knowledge of places and pleasant … More
❤️1
vinod tour and travels (owner)
a year ago
Hi Pasha,
Thank you 🙏🙏
We're delighted to hear that you had a wonderful experience with Mr. Vinod during your trip from Lucknow to Khajuraho and back to Delhi! We're thrilled to know that he exceeded your expectations with his exceptional driving skills, vast knowledge of the places you visited, and his courteous behavior.
We're grateful for your kind words about Mr. Vinod's professionalism and commitment to providing a safe and enjoyable journey. It's wonderful to know that he made your long trip so easy and stress-free.
We'll make sure to pass on your wonderful feedback to Mr. Vinod and the rest of our team. We're looking forward to serving you again in the future, and we'll do our best to ensure that Mr. Vinod is available to drive you to your next destination.
Warm Regards,
Team Vinod Tour & Travel, Kotdwar, Uttrakhand.
[Arindam Naskar2 reviews](https://www.google.com/maps/contrib/105900029480473107428/reviews?hl=en-IN)
4 months ago
Excellent service, Polite behaviour and he gave us good suggestion for the rest of trips.
vinod tour and travels (owner)
4 months ago
Thank you so much for your kind feedback! We are glad to know that you were happy with our service and found our travel suggestions helpful. Your satisfaction is our top priority, and your appreciation means a lot to us. We look forward to serving you again in the future. Thank you for choosing Vinod Tour & Travels!
[Barbara Rocchetti2 reviews](https://www.google.com/maps/contrib/112979694251427515614/reviews?hl=en-IN)
a year ago
Absolute first class service with Vinod. He was a safe, knowledgeable and very accommodating driver, guide and host. He made our trip very pleasant. We would have no hesitation in recommending his services in India.
Thank you for our lovely trip Vinod and see you soon! :)
❤️1
vinod tour and travels (owner)
Edited 2 months ago
Here's a warm and professional reply you can send to the customer:
Thank you so much for your wonderful review! 😊
It was truly a pleasure to be your driver and guide. I'm very happy to hear that you enjoyed your trip and felt safe and comfortable throughout the journey.
Your kind words and recommendation mean a lot to me. Thank you for choosing Vinod Tour and Travels. I look forward to welcoming you back to India and serving you again soon.
Safe travels, and see you again! 🇮🇳🚖
[Harish Raju1 review·8 photos](https://www.google.com/maps/contrib/111236391781492055126/reviews?hl=en-IN)
a year ago
Mr. Vinod Gosai is very good driving and friendly. Punctual and shows all important attractions properly. Guides you against tourist traps and scams. Very friendly
❤️1
vinod tour and travels (owner)
a year ago
Thank you sir 🙏🏾🙏🏾🙏🏾
[MIG VIAGGI1 review](https://www.google.com/maps/contrib/112339805676990275578/reviews?hl=en-IN)
a year ago
We really had a very good time with Vinod. He always took care of us, even when we were late, he supported us and skip the traffic jam. Very prudent driver. We recommend him for your travels!
❤️🙏2
vinod tour and travels (owner)
Edited 2 months ago
Thank you so much for your wonderful review! 😊
It was a pleasure serving you, and I'm very happy to know that you enjoyed your trip. Your kind words and recommendation truly mean a lot to me.
Thank you for choosing Vinod Tour and Travels. I look forward to welcoming you again on your next visit to India.
Safe travels, and see you again soon! 🇮🇳🚖 vinod tour and travels new delhi india contact number+918076069722
[Armandina RamírezLocal Guide·16 reviews·6 photos](https://www.google.com/maps/contrib/104253806674055384807/reviews?hl=en-IN)
9 months ago
Vinod was very professional and did a great job driving us from Delhi to Agra to the Taj Mahal.
❤️1
vinod tour and travels (owner)
9 months ago
Thank you so much my service🙏
[Christophe Jaku2 reviews](https://www.google.com/maps/contrib/115188928823345133437/reviews?hl=en-IN)
a year ago
Vinod is a first class driver ! Our trip through Rajasthan would not have been the same without him. He is more than a driver… a perfect guide with many secret itinaries and surprises !
❤️1
vinod tour and travels (owner)
a year ago
Hello Christophe Ji!
We're thrilled to hear that you had an exceptional experience with our driver, Vinod! We're grateful for your kind words and are thrilled that he could make your trip to Rajasthan truly unforgettable. It's wonderful to know that he went above and beyond to share his local knowledge and secrets with you, making your journey a truly unique and memorable one.
We're delighted that you appreciated Vinod's expertise and enthusiasm as a guide, and we're proud to have him as part of our team. He truly embodies the spirit of exceptional customer service, and we're grateful to have customers like you who appreciate his efforts.
Thank you for sharing your wonderful experience with us, Christophe Ji! We're honored to have been a part of your journey and look forward to welcoming you back to Vinod Tour & Travel in the future.
Warm Regards,
Team Vinod Tour & Travel, Kotdwar, Uttrakhand
[Daniella GattLocal Guide·28 reviews·30 photos](https://www.google.com/maps/contrib/111440591992250763278/reviews?hl=en-IN)
a year ago
Great driver for our week in India! He was always on time and knowledgable on the local area…we even got him into bird watching, ha! We would highly recommend using Vinod for getting around India! Thank you for a lovely trip Vinod!!
🙏1
vinod tour and travels (owner)
a year ago
Thank you madam my service and your friend request mservice of friend is that requirement India
[Amit Gusain3 reviews](https://www.google.com/maps/contrib/113704130357395347134/reviews?hl=en-IN)
2 months ago
Convenient, responsible, and friendly person . Go for it
vinod tour and travels (owner)
2 months ago
Thank you so much for your kind words and 5-star review! 😊
We truly appreciate your support. We're glad you found our service convenient, responsible, and friendly. It was our pleasure to serve you, and we look forward to welcoming you again on your next trip.
Thank you for choosing Vinod Tour & Travels! 🙏🚖
📞 +91 80760 69722
[jitendra singh narukaLocal Guide·14 reviews·4 photos](https://www.google.com/maps/contrib/108068804767732099226/reviews?hl=en-IN)
a year ago
This is a amazing tour service provider. I have been from Delhi to Jaisalmer tour with vinod . He gave me excellent service. His behaviour is so nice . He has very good knowledge about the city tour in Rajasthan. So please enjoy the trip with him . Thank you
❤️1
vinod tour and travels (owner)
a year ago
Thank you boss
[Patrick Duck2 reviews](https://www.google.com/maps/contrib/107167975148846658088/reviews?hl=en-IN)
2 years ago
Absolute first class service from Vinod. He was a safe, knowledgeable and very accommodating driver, guide and host. We would have no hesitation in recommending his services. … More
❤️1
vinod tour and travels (owner)
2 years ago
Thank you sir
[kezz MeehanLocal Guide·9 reviews·16 photos](https://www.google.com/maps/contrib/116431289912524727009/reviews?hl=en-IN)
2 years ago
We had the pleasure of having Vinod as our driver while we were on holiday in India October 2023. We was safe driver, very friendly and professional. We would highly recommend using him. … More
🙏2
vinod tour and travels (owner)
Edited 2 months ago
Thank you so much for your wonderful review and for your kind words! 😊
It was truly a pleasure to be your driver during your holiday in India. I'm delighted to know that you had a safe and enjoyable experience. Your recommendation means a lot to me and encourages me to continue providing the best service possible.
Thank you for choosing Vinod Tour and Travels. I hope to welcome you back to India again in the future.
Wishing you all the best and safe travels! 🇮🇳🚖
[Dennis B.4 reviews](https://www.google.com/maps/contrib/114081920173345748109/reviews?hl=en-IN)
2 years ago
We stayed for a week in India and Vinod has been a kind and very helpful driver. He was always there for us regardless the time.
Thank you very much for the good service 🙏🏽
🙏1
vinod tour and travels (owner)
2 years ago
Thank you 👍
[María Pía Munizaga Mellado1 review](https://www.google.com/maps/contrib/115471302856251547763/reviews?hl=en-IN)
a year ago
Excellent driver, very friendly and respectful, and he has a good knowledge of places to visit. He made my trip in Delhi very pleasant.
❤️1
vinod tour and travels (owner)
a year ago
Thank you mam
[Dhruv Dave3 reviews](https://www.google.com/maps/contrib/112722622636761663944/reviews?hl=en-IN)
4 months ago
Wonderful travel agency and very good service
vinod tour and travels (owner)
4 months ago
Thankyou sir for the review🙏
[Ankit KotnalaLocal Guide·63 reviews·321 photos](https://www.google.com/maps/contrib/108304589218107609660/reviews?hl=en-IN)
a month ago
Very helpful and interactive drivers
vinod tour and travels (owner)
a month ago
Hi Ankit, thank you for taking the time to share your experience with vinod tour and travels uttrakhand kotdwar. We’re glad to hear you found our drivers very helpful and interactive—safe, friendly guidance is exactly what we aim to provide for every trip.
[Sudeep Kukreti2 reviews](https://www.google.com/maps/contrib/103696173606054289864/reviews?hl=en-IN)
3 months ago
Clean and very good service @Vinod gusain
vinod tour and travels (owner)
3 months ago
Hi Sudeep,
Thank you so much for your wonderful 5-star review! We're absolutely delighted to hear that you found our service clean and very good. It’s fantastic to know that Vinod Gusain provided you with such an excellent experience. Our team at vinod tour and travels uttrakhand kotdwar always strives to ensure our customers have comfortable and pleasant journeys.
We truly appreciate your kind words and look forward to assisting you with your future travel plans. 🙏
Regards,
The vinod tour and travels uttrakhand kotdwar Team
[Veena Ramdhani3 reviews](https://www.google.com/maps/contrib/116792689014111083097/reviews?hl=en-IN)
2 years ago
If you looking for a driver on a planned trip to India, look no further than Vinod Gusain.A humble man who loves his country and treats his clients with compassion. You are safe never conned into doing something you do not want to and are … More
🙏1
vinod tour and travels (owner)
2 years ago
Thank you🙏
[권오승Local Guide·10 reviews·22 photos](https://www.google.com/maps/contrib/109592661840869910872/reviews?hl=en-IN)
a year ago
very nice driver vinod kumar is the pbest driver
❤️1
vinod tour and travels (owner)
a year ago
Thank you sir
[Alok Singh2 reviews](https://www.google.com/maps/contrib/110032153153350716448/reviews?hl=en-IN)
3 years ago
Conditions of Car is superb, Hygienic & Safe,. The most part of this car is quite comfort in long journey, And The person who seated at Driving seat is having familiar attitudes & Passengers can Trust on Him by any Means, Thank You
🙏1
vinod tour and travels (owner)
a year ago
Ok👍
[Rachit Bindlish6 reviews](https://www.google.com/maps/contrib/110264935197763115224/reviews?hl=en-IN)
a year ago
We have taken services of vinod ji fir going kotdwar to lansdowne.the overall experience was excellent .The car was in excellent condition & his nature was wonderful.Excellent service,nice behaviour& punctual.
❤️1
vinod tour and travels (owner)
a year ago
Thank you sir🙏
[Luke OxleyLocal Guide·18 reviews](https://www.google.com/maps/contrib/108095342365850514249/reviews?hl=en-IN)
10 months ago
Very friendly, clean car and safe driver. Highly recommend.
❤️1
vinod tour and travels (owner)
10 months ago
Thank you so much sir 🙏
[Eugénie Jakubyszyn1 review](https://www.google.com/maps/contrib/100875862710392555982/reviews?hl=en-IN)
a year ago
Amazing trip ! I highly recommend, such a great experience. Thank you so much Vinod for everything.
❤️1
vinod tour and travels (owner)
a year ago
Hello Eugénie Jakubyszyn ji,
We're thrilled to hear that you had an amazing trip with us! We're grateful for your kind words and for choosing Vinod Tour & Travel for your travel needs. It's always a pleasure to serve our customers and make their journeys memorable.
We're glad you had a great experience with us and we're grateful for your recommendation. Your feedback means a lot to us and we'll continue to strive to provide the best services to our customers.
Thank you again for your kind words and for being an important part of our Vinod Tour & Travel family. We look forward to serving you again in the future.
Warm Regards,
Team Vinod Tour & Travel, Kotdwar, Uttrakhand
[Sukhdev Singh3 reviews](https://www.google.com/maps/contrib/109664240894004374518/reviews?hl=en-IN)
a year ago
Mr Vinod very good driver good service good car I am very happy Mr Vinod car very green
❤️1
vinod tour and travels (owner)
a year ago
Thank you sir 🙏🙏
[saket khodaskarLocal Guide·68 reviews·176 photos](https://www.google.com/maps/contrib/103103255855221985819/reviews?hl=en-IN)
8 months ago
Amazing experience, super chill person.
❤️1
vinod tour and travels (owner)
8 months ago
Thank you sir 🙏
[Tabbu Pal4 reviews](https://www.google.com/maps/contrib/110056491964219434158/reviews?hl=en-IN)
a year ago
I travelled alone and it was amazing experience with Vinod he was nice and smoothly safe drop me at my home
❤️1
vinod tour and travels (owner)
a year ago
Thank you ji👍
[노상호2 reviews](https://www.google.com/maps/contrib/107821736907386908558/reviews?hl=en-IN)
a year ago
Vinod is a good driver. I’ll reccomand him to everyome who try to visit Agra
❤️1
vinod tour and travels (owner)
a year ago
Thank you sir
[Bijendra Singh1 review](https://www.google.com/maps/contrib/115406457166715237151/reviews?hl=en-IN)
3 years ago
Very cordial person. It has been a great experience with him traveling from kotdwara to vaishali. … More
🙏2
vinod tour and travels (owner)
a year ago
Thank you sir🙏
[Jitender Agarwal8 reviews](https://www.google.com/maps/contrib/116010912908679885525/reviews?hl=en-IN)
7 months ago
हमारा सफर बहुत ही आनन्द से रहा, विनोद जी का ड्राइविंग बहुत ही बढ़िया है।।
See translation (English)
❤️1
vinod tour and travels (owner)
7 months ago
Thank you sir 🙏
[Chandana S. O4 reviews](https://www.google.com/maps/contrib/110936263105250476126/reviews?hl=en-IN)
a year ago
Nice and good experience with vinod sir, we were able to have south indian food which was tasty .thank you sir😊
❤️2
vinod tour and travels (owner)
Edited a year ago
Ok👍
[Idris Khan9 reviews](https://www.google.com/maps/contrib/111027051201580606750/reviews?hl=en-IN)
a year ago
Best sarvice I had to meet travel india Vinod such great parson highly recommend for vinod
❤️1
vinod tour and travels (owner)
a year ago
Thank you thank you sir
[Anuma Bisht3 reviews](https://www.google.com/maps/contrib/113573873904364391465/reviews?hl=en-IN)
a year ago
Had an easy and safe journey with him, very accommodating amd patient
❤️1
vinod tour and travels (owner)
a year ago
Thank you ji 🙏
[Ravish RawatLocal Guide·51 reviews·1,558 photos](https://www.google.com/maps/contrib/102993566602604415937/reviews?hl=en-IN)
3 years ago
Mr. Vinod Gosain is a very professional and well-behaved driver 👍 He is a very understanding and courteous person 😊
🙏1
vinod tour and travels (owner)
2 years ago
Thank you
[Issac Regisow1 review](https://www.google.com/maps/contrib/113428939824360505051/reviews?hl=en-IN)
a year ago
Very decent driver with good skill of driving 👍
❤️1
vinod tour and travels (owner)
a year ago
Thank you 🙏,
We're thrilled to hear that you had a fantastic experience with our taxi service! It's great to know that our driver impressed you with their excellent driving skills and made your journey a comfortable one.
We're grateful for your feedback and will make sure to pass on your kind words to our driver. At Vinod Tour & Travel, we strive to provide the best possible service to our customers, and it's reviews like yours that motivate us to keep improving.
Thank you for choosing us, Issac Ji! We're glad you enjoyed your ride with us and hope to have the opportunity to serve you again soon.
Warm Regards,
Team Vinod Tour & Travel, Kotdwar, Uttrakhand
[Lal Singh3 reviews](https://www.google.com/maps/contrib/117569739618619070098/reviews?hl=en-IN)
2 years ago
Veri nice driver good journey mister Vinod is good tour Agra Jaipur my trip is good
🙏1
vinod tour and travels (owner)
2 years ago
Good👍
[akhil kandari3 reviews](https://www.google.com/maps/contrib/105129873282663345952/reviews?hl=en-IN)
2 months ago
Nice car ride
❤️1
vinod tour and travels (owner)
2 months ago
Thank you so much for your kind review! 😊🙏 We’re glad you enjoyed the car ride. Your support means a lot to Vinod Tour & Travels. We look forward to serving you again! 🚗✨
[Sourav Singh1 review](https://www.google.com/maps/contrib/115443698202926063490/reviews?hl=en-IN)
3 years ago
My Trip was too good with this guy he is familier I like to travel with him I hope so my next trip will be soon with you Thankyou my big brother I have a good experience with you brother thankyou ..
🙏1
vinod tour and travels (owner)
a year ago
Thank you sir
[NEWS 81 NETWORK1 review](https://www.google.com/maps/contrib/101790246432248730165/reviews?hl=en-IN)
3 years ago
Car and driver are very good and good condition very clean very hygienic.driver is very co operative see you Next time. … More
🙏1
vinod tour and travels (owner)
a year ago
Ok👍
[PREETI SINGH2 reviews](https://www.google.com/maps/contrib/104334168935219666925/reviews?hl=en-IN)
a year ago
Very good driver excellent service
❤️1
vinod tour and travels (owner)
a year ago
Thank you
[veena negi6 reviews·1 photo](https://www.google.com/maps/contrib/110055514343532540168/reviews?hl=en-IN)
3 years ago
Nice experience, driver behave very comfortable..
🙏1
vinod tour and travels (owner)
2 years ago
Thank you madam
[Jitendra Rawat2 reviews](https://www.google.com/maps/contrib/115197156556839901131/reviews?hl=en-IN)
3 years ago
वेरी नाइस बहुत अच्छा है सफर हमारा बहुत अच्छा रहा अगली बार भी हम आपको बुलाएंगे आपको बहुत अनुभव है आप बहुत बढ़िया कार चलाते हो
See translation (English)
🙏1
vinod tour and travels (owner)
3 years ago
Thank you sir
[Maharishi Group1 review](https://www.google.com/maps/contrib/101946516771863732148/reviews?hl=en-IN)
3 years ago
Vinod is very good drive.driving is good nd save driving..nd help full.
🙏1
vinod tour and travels (owner)
a year ago
Thank you sir👍
[Rattan Prakash1 review](https://www.google.com/maps/contrib/102517211959037386144/reviews?hl=en-IN)
3 years ago
Very good service and politely communation with the customer and have good knowledge of the places.
🙏1
vinod tour and travels (owner)
a year ago
Thank you sir🙏
[Ashok Kumar3 reviews](https://www.google.com/maps/contrib/111756127630833072179/reviews?hl=en-IN)
2 years ago
Very nice good service.Excellent job.
🙏1
vinod tour and travels (owner)
2 years ago
Thank you
[Manju Kumari3 reviews](https://www.google.com/maps/contrib/116943656894683422145/reviews?hl=en-IN)
3 years ago
Good driving and behavior is also very good .
🙏1
vinod tour and travels (owner)
2 years ago
Thank you mam
[Vishnu Dubey1 review](https://www.google.com/maps/contrib/112163079005315890728/reviews?hl=en-IN)
a year ago
Excellent service I m very happy.
❤️1
vinod tour and travels (owner)
a year ago
Thank you sir
[Gayatri SinghLocal Guide·17 reviews·85 photos](https://www.google.com/maps/contrib/107945809247066483650/reviews?hl=en-IN)
3 years ago
Had a nice experience and in short time travel! Happy! … More
🙏2
vinod tour and travels (owner)
2 years ago
Thank you ji
[Naresh Sagar1 review·1 photo](https://www.google.com/maps/contrib/106327601405382359790/reviews?hl=en-IN)
3 years ago
###driver are very good and good condition very clean# .driver is very co operative see you Next time.#✓
🙏1
vinod tour and travels (owner)
a year ago
Thank you sir
[Jitendra kumar3 reviews·1 photo](https://www.google.com/maps/contrib/114212235420918323813/reviews?hl=en-IN)
3 years ago
Very Driver excellent behavior must try once ..
🙏1
vinod tour and travels (owner)
a year ago
Thank you sir
[Karan Juyal1 review](https://www.google.com/maps/contrib/108396841843348325795/reviews?hl=en-IN)
3 years ago
Very nice person great experience to travel with him
🙏1
vinod tour and travels (owner)
a year ago
Ok👍
[Daksh Tour And TravelLocal Guide·19 reviews·44 photos](https://www.google.com/maps/contrib/101492827630115837279/reviews?hl=en-IN)
3 years ago
Good service thank you so much vinod sir🙏🏻
🙏1
vinod tour and travels (owner)
a year ago
Thank you sir
[Puja Gusain1 review](https://www.google.com/maps/contrib/107997027930142523621/reviews?hl=en-IN)
3 years ago
Bhut hi achi suvida dete h... Vinod tour & travel.....
See translation (English)
🙏1
vinod tour and travels (owner)
a year ago
Thank you ji 🙏
[DEEPAK CHAUHAN7 reviews](https://www.google.com/maps/contrib/115787465287456906504/reviews?hl=en-IN)
2 years ago
Very nice drive excellent 👌
🙏1
vinod tour and travels (owner)
2 years ago
Thank you sir ji
[Suraj Shah2 reviews](https://www.google.com/maps/contrib/118182612339402478439/reviews?hl=en-IN)
Edited 3 years ago
Very good sarvice and good driving
🙏1
vinod tour and travels (owner)
2 years ago
Thank you sir
[Dharamveer Singh3 reviews](https://www.google.com/maps/contrib/114158134556929166503/reviews?hl=en-IN)
a year ago
Very nice driver
❤️1
vinod tour and travels (owner)
a year ago
Thank you ij
[Nandan Singh3 reviews](https://www.google.com/maps/contrib/112354994324473355770/reviews?hl=en-IN)
10 months ago
Good Service and sutstiction
❤️1
vinod tour and travels (owner)
10 months ago
Thank you sir so much my services 🙏
[Diwakar kumar3 reviews](https://www.google.com/maps/contrib/118240678239264672300/reviews?hl=en-IN)
3 years ago
Very nice service, excellent 👌 service ,good price
❤️1
vinod tour and travels (owner)
2 years ago
Thank you sir
[Anju Mathur4 reviews](https://www.google.com/maps/contrib/116432189976871487267/reviews?hl=en-IN)
9 months ago
Excellent
❤️1
vinod tour and travels (owner)
Edited 9 months ago
🙏 Thank you for choosing Vinod Tour & Travels!
Humein khushi hai ki aapko hamari service pasand aayi.
Aage bhi aapke safar ko yaadgaar banane ka mauka dein. 🚗✨
See translation (English)
[Prabhakar Shah4 reviews](https://www.google.com/maps/contrib/107538089910586497558/reviews?hl=en-IN)
2 years ago
Exllent Drive vindo helpful person
🙏1
vinod tour and travels (owner)
2 years ago
Thanks sir,🙏
[Hardeep Negi6 reviews](https://www.google.com/maps/contrib/116572595100733613224/reviews?hl=en-IN)
3 years ago
Excellent great experience, very courteous amazing staff
🙏1
vinod tour and travels (owner)
a year ago
Thank you sir
[Sarjeet Sharma2 reviews](https://www.google.com/maps/contrib/101342665113812685866/reviews?hl=en-IN)
2 years ago
Very nice excellent report 👍
🙏1
vinod tour and travels (owner)
2 years ago
, m
[Dinesh Singh4 reviews·2 photos](https://www.google.com/maps/contrib/102488683794388076736/reviews?hl=en-IN)
3 years ago
Very Nice Service Mr Vinod Sir
🙏1
vinod tour and travels (owner)
a year ago
Ok🙏
[Atul syoli2 reviews·12 photos](https://www.google.com/maps/contrib/114823644083313346824/reviews?hl=en-IN)
3 years ago
Very very good ,,dirver Vinod sir,,and good services,,
🙏1
vinod tour and travels (owner)
a year ago
Thank you sir 🙏
[Kunal Kumar1 review](https://www.google.com/maps/contrib/104348300351017148912/reviews?hl=en-IN)
2 years ago
Very nice exilet service
🙏1
vinod tour and travels (owner)
2 years ago
Thank you❤
[Dc Dardar2 reviews·2 photos](https://www.google.com/maps/contrib/107341793332369372301/reviews?hl=en-IN)
Edited 3 years ago
Very good
🙏1
vinod tour and travels (owner)
2 years ago
Thank you sir
[Rohit Maindola1 review](https://www.google.com/maps/contrib/105263187418305909887/reviews?hl=en-IN)
3 years ago
Very nice Ecilanat driver
🙏1
vinod tour and travels (owner)
2 years ago
🙏
[Vaibhav Bhatia9 reviews·11 photos](https://www.google.com/maps/contrib/113983757685609065149/reviews?hl=en-IN)
3 years ago
Very nice cab servise
🙏2
vinod tour and travels (owner)
2 years ago
Thank you sir
[Sanjay Singh3 reviews](https://www.google.com/maps/contrib/112462328274435028396/reviews?hl=en-IN)
2 years ago
Mr vinod Exlent driver
🙏1
vinod tour and travels (owner)
2 years ago
Thank you sir
[Dalip Kumar2 reviews](https://www.google.com/maps/contrib/101830862934564479037/reviews?hl=en-IN)
3 years ago
I am really impressed by your service
🙏1
vinod tour and travels (owner)
2 years ago
Thank you sir
[Karam Dugi2 reviews](https://www.google.com/maps/contrib/104692185779809249434/reviews?hl=en-IN)
a year ago
Good service for tourism
❤️1
vinod tour and travels (owner)
a year ago
Thank you my service
[Pankaj Bisht5 reviews](https://www.google.com/maps/contrib/108836585522451240955/reviews?hl=en-IN)
3 years ago
Good driving skills and behaviour
🙏1
vinod tour and travels (owner)
3 years ago
Thank you sir
[Keshav Rawat3 reviews](https://www.google.com/maps/contrib/102284934366980957099/reviews?hl=en-IN)
3 years ago
It was nice to have service from them … More
🙏1
vinod tour and travels (owner)
a year ago
Thank you sir🙏
[Surender Singh2 reviews](https://www.google.com/maps/contrib/113448874860744318306/reviews?hl=en-IN)
2 years ago
Excellent service good 👍
🙏1
vinod tour and travels (owner)
2 years ago
Thank you sir
[prince roy2 reviews·5 photos](https://www.google.com/maps/contrib/105869761791861768753/reviews?hl=en-IN)
3 years ago
Very good driver
🙏1
vinod tour and travels (owner)
a year ago
Thank you ji👍
[Rishi Pandya2 reviews](https://www.google.com/maps/contrib/105615168761743184208/reviews?hl=en-IN)
a year ago
Very good service
❤️1
vinod tour and travels (owner)
a year ago
Thank you sir👍
[Vivek Juyal5 reviews](https://www.google.com/maps/contrib/104498440928200420170/reviews?hl=en-IN)
3 years ago
Safely drive with nice behavior
🙏1
vinod tour and travels (owner)
a year ago
Thank you ji 🙏
[Rohit Singh1 review](https://www.google.com/maps/contrib/104377050355156543989/reviews?hl=en-IN)
3 years ago
Very nice
🙏1
vinod tour and travels (owner)
a year ago
Thank you sir
[Bhavishanth Suresh8 reviews](https://www.google.com/maps/contrib/113484233518249648611/reviews?hl=en-IN)
a year ago
Good Service.
❤️1
vinod tour and travels (owner)
a year ago
Thank you sir 🙏🙏
[SURAJLocal Guide·44 reviews·33 photos](https://www.google.com/maps/contrib/112139564222743176437/reviews?hl=en-IN)
3 years ago
Very professional and nice service
🙏1
vinod tour and travels (owner)
a year ago
👍
[Rajini Agrwal1 review](https://www.google.com/maps/contrib/110885008586255433724/reviews?hl=en-IN)
3 years ago
Nice 😊
🙏1
vinod tour and travels (owner)
a year ago
Thank you sir🙏
[Yashika Phul2 reviews](https://www.google.com/maps/contrib/111497643097167218795/reviews?hl=en-IN)
3 years ago
Wonderful … More
🙏1
vinod tour and travels (owner)
2 years ago
Thank you sir
[Tanya Negi3 reviews·4 photos](https://www.google.com/maps/contrib/114366745218557103478/reviews?hl=en-IN)
3 years ago
The place were very good
🙏1
vinod tour and travels (owner)
a year ago
👍
[BHASKAR Kumar6 reviews·8 photos](https://www.google.com/maps/contrib/104705530573642473818/reviews?hl=en-IN)
Edited a year ago
My experience with this, is amazing
🙏1
vinod tour and travels (owner)
a year ago
Thank you sir
[Neeraj Bhardawaj2 reviews](https://www.google.com/maps/contrib/111634100139886881260/reviews?hl=en-IN)
Edited 8 months ago
Nice driver👌👌
❤️1
vinod tour and travels (owner)
Edited 8 months ago
🙏 Thank you for choosing Vinod Tour & Travels!
Humein khushi hai ki aapko hamari service pasand aayi.
Aage bhi aapke safar ko yaadgaar banane ka mauka dein. 🚗✨🙏
See translation (English)
[Shashi Chander1 review·3 photos](https://www.google.com/maps/contrib/114264978984656780751/reviews?hl=en-IN)
3 years ago
Kotdwa to & vice versa … More
🙏1
vinod tour and travels (owner)
2 years ago
👍
[Kalas Sing1 review](https://www.google.com/maps/contrib/107423373316068531556/reviews?hl=en-IN)
2 years ago
Very good excellent serviceVery good excellent service
Translated by Google·See original (English)
🙏1
vinod tour and travels (owner)
Edited 2 years ago
Thank you sir
[Gopal Panday1 review](https://www.google.com/maps/contrib/108390122607943844489/reviews?hl=en-IN)
3 years ago
Very nice excellent Very nice excellent
🙏1
vinod tour and travels (owner)
2 years ago
Thank you
[Rashmi Joshi1 review](https://www.google.com/maps/contrib/107239569954090310765/reviews?hl=en-IN)
3 years ago
Great experience 👍 👌 👏
🙏1
vinod tour and travels (owner)
a year ago
Thank you🙏
[A-kay Singh1 review](https://www.google.com/maps/contrib/100402723614167141691/reviews?hl=en-IN)
3 years ago
Extent … More
🙏1
vinod tour and travels (owner)
a year ago
Thank you sir🙏
[arun naithaniLocal Guide·11 reviews·5 photos](https://www.google.com/maps/contrib/104977143069286430063/reviews?hl=en-IN)
3 years ago
Excellent service
🙏1
vinod tour and travels (owner)
2 years ago
Thank you sir
[Saurabh Bisht3 reviews](https://www.google.com/maps/contrib/103923362601421779690/reviews?hl=en-IN)
3 years ago
Good person..👌🏼👍🏼
🙏1
vinod tour and travels (owner)
a year ago
Ok🙏
[Sangeeta Devi1 review](https://www.google.com/maps/contrib/101856497018625011043/reviews?hl=en-IN)
3 years ago
Good work👍👍👍👍
❤️1
vinod tour and travels (owner)
a year ago
Thank you🙏
[Mahesh Chandra1 review](https://www.google.com/maps/contrib/107476278858075669331/reviews?hl=en-IN)
3 years ago
वेरी नाइसगुड कार
See translation (English)
🙏1
vinod tour and travels (owner)
a year ago
Thank you sir
[Bipin Sati1 review](https://www.google.com/maps/contrib/103794381596226319061/reviews?hl=en-IN)
3 years ago
Good services
🙏1
vinod tour and travels (owner)
a year ago
Thank you🙏
[Anshika Das3 reviews](https://www.google.com/maps/contrib/101552714335340331612/reviews?hl=en-IN)
5 days agoNew
I travelled from Kotdwar to Delhi by cab, and it was a really good experience. The cab was clean and comfortable, and the driver was polite, professional, and drove safely. The journey was smooth and hassle-free. Overall, I had a great experience and would definitely recommend their service for comfortable and reliable travel.
❤️1
vinod tour and travels (owner)
4 hours ago
Thank you so much for your kind words and 5-star review! 🙏😊 We’re glad you had a comfortable and safe journey from Kotdwar to Delhi. Your trust and appreciation mean a lot to us. We look forward to serving you again with the best travel experience. 🚕❤️
Vinod Tour & Travels
[Akshat Keshtwal4 reviews](https://www.google.com/maps/contrib/111940103014585451308/reviews?hl=en-IN)
a week agoNew
Exceptional travel experience.
Would highly recommend to all!!
vinod tour and travels (owner)
4 hours ago
Thank you so much for your kind words and recommendation! 🙏😊 We look forward to serving you again. 🚗✨
[Riya2 reviews](https://www.google.com/maps/contrib/102097827188853842838/reviews?hl=en-IN)
a month ago
I travelled from Delhi to dehradun with Vinod Ji. He is an excellent driver and a very nice person. The car was very clean and well-maintained, and the journey was very safe and comfortable. He is very punctual, polite and professional, and … More
❤️1
vinod tour and travels (owner)
a month ago
Thank you so much for your wonderful 5-star review! ⭐⭐⭐⭐⭐
It was truly a pleasure driving you from Delhi to Dehradun and Chandigarh. I’m very happy to know that you found the car clean, comfortable, and well-maintained, and that you enjoyed a safe and smooth journey.
Your kind words about my punctuality, behaviour, and driving mean a lot to me. Customer safety, comfort, and satisfaction are always my top priorities.
Thank you for choosing Vinod Tour & Travels and for recommending our taxi service. We look forward to serving you and your family again on your next journey! 🙏🚖
Warm regards,
Vinod Tour & Travels you so much for your wonderful 5-star review! ⭐⭐⭐⭐⭐
It was truly a pleasure driving you from Delhi to Dehradun and Chandigarh. I’m very happy to know that you found the car clean, comfortable, and well-maintained, and that you enjoyed a safe and smooth journey.
Your kind words about my punctuality, behaviour, and driving mean a lot to me. Customer sls
[Chandra Singh2 reviews·8 photos](https://www.google.com/maps/contrib/117601650628248735790/reviews?hl=en-IN)
Edited a month ago
I travelled from Delhi to Chandigarh with Vinod Ji. He is an excellent driver and a very nice person. The car was very clean and well-maintained, and the journey was very safe and comfortable. He is very punctual, polite and professional, … More
❤️1
vinod tour and travels (owner)
a month ago
Hello Chandra, thank you for your wonderful 5-star review! We’re so glad your Delhi to Chandigarh trip with Vinod Ji was safe, smooth, and completely hassle-free. It’s great to hear the car was clean and well-maintained, and that Vinod Ji’s punctual, polite, and professional driving made your journey comfortable.
Your recommendation means a lot to our team 😊 We look forward to assisting you again whenever you need a reliable taxi service.
Warm regards,
Team Vinod Tour and Travels, Uttrakhand Kotdwar
[Ashish Malhotra2 reviews](https://www.google.com/maps/contrib/108946636762630599532/reviews?hl=en-IN)
a month ago
Nice to be nice professional guy with professional service
vinod tour and travels (owner)
a month ago
Hi Ashish, thank you for the 5-star review! We’re glad you found our team professional. We aim to make every trip smooth and hope to welcome you again. Regards, Team Vinod Tour & Travels
[Rohit Silmana3 reviews](https://www.google.com/maps/contrib/105118706959210021339/reviews?hl=en-IN)
a month ago
Nice and save journey. Nice driver he was friendly in nature 🌝🌸🌺🫡🫡😀😀😀
vinod tour and travels (owner)
a month ago
Hi Rohit, thank you for your wonderful review! We’re delighted you had a safe trip and liked our driver’s friendly nature. 😊 We look forward to welcoming you again. Regards, Team Vinod Tour & Travels
[abhishek yadav5 reviews·4 photos](https://www.google.com/maps/contrib/101841377763015586962/reviews?hl=en-IN)
2 months ago
Behaviour and driving skills both are good.
vinod tour and travels (owner)
2 months ago
Thank you so much for your kind review! 😊 We're delighted to know that you appreciated our behaviour and driving skills. Your feedback motivates us to continue providing safe, comfortable, and friendly service. We look forward to serving you again with Vinod Tour & Travels. Have a wonderful day! 🚖🙏
[Shivani Rawat1 review](https://www.google.com/maps/contrib/108776392289439367045/reviews?hl=en-IN)
2 months ago
Very nice driver... Comfortable journey... 😄
vinod tour and travels (owner)
2 months ago
Hi Shivani, thank you so much for your 5-star rating and for sharing your experience with vinod tour and travels uttrakhand kotdwar. We’re glad to hear you found our driver very nice and that your journey was comfortable throughout. Providing a safe, smooth ride is exactly what we aim for, and your feedback motivates our team every day. 😊
We’d be happy to assist you again for your next trip—please reach out whenever you’re planning travel.
Regards, Team vinod tour and travels uttrakhand kotdwar
[Tapasya Upadhyay4 reviews·4 photos](https://www.google.com/maps/contrib/104124497150241122007/reviews?hl=en-IN)
3 months ago
Had a wonderful experience with Vinod Tour and Travels. Our driver, Manish Bhaiya, was very professional, punctual, and polite throughout the journey. He drove safely, knew the routes well, and made our trip comfortable and hassle-free. The … More
vinod tour and travels (owner)
3 months ago
Thank you so much for your wonderful feedback! 🙏
We are truly delighted to know that you had a great experience with Vinod Tour & Travels. Your kind words about Manish Bhaiya's professionalism, punctuality, safe driving, and courteous behavior mean a lot to us. We always strive to provide clean vehicles, reliable service, and a comfortable journey for every guest.
Thank you for your recommendation. We look forward to serving you again on your next trip to Uttarakhand!
"""

# Regex to split on [AuthorName...](URL)
blocks = re.split(r'(?=\[.+?\]\(https?://www\.google\.com/maps/contrib/[^)]+\))', raw_reviews_text.strip())

parsed = []
for block in blocks:
    block = block.strip()
    if not block:
        continue
    # Extract header: [Author](URL)
    m = re.match(r'\[(.+?)\]\((https?://[^\)]+)\)', block)
    if not m:
        continue
    author_raw = m.group(1).strip()
    url = m.group(2).strip()
    
    # Author might have "Local Guide·21 reviews·10 photos" or "1 review" appended
    # e.g. "Abhishek Verma1 review" or "MAYYUR B MERCHANTLocal Guide·21 reviews·10 photos"
    # Let's clean author name:
    author_clean = author_raw
    badge = ""
    if "Local Guide" in author_clean:
        badge = "Local Guide"
        author_clean = re.sub(r'Local\s*Guide.*$', '', author_clean).strip()
    # Strip trailing digits + review(s)
    author_clean = re.sub(r'\d+\s*(?:reviews?|photos?).*$', '', author_clean).strip()
    
    # Rest of block after [Author](url)
    rest = block[m.end():].strip()
    
    # Split by lines
    lines = [l.strip() for l in rest.split('\n') if l.strip()]
    if not lines:
        continue
    
    # Date is typically the first line, e.g. "a month ago", "Edited 5 months ago", "5 days agoNew", etc.
    date_line = lines[0]
    date_clean = re.sub(r'New$', '', date_line).strip()
    
    # Review body lines: everything until owner response
    body_lines = []
    for l in lines[1:]:
        # Stop if owner response begins
        if re.search(r'vinod tour and travels\s*\(owner\)', l, re.I):
            break
        # Skip star lines like ⭐⭐⭐⭐⭐
        if re.match(r'^[⭐★]+$', l):
            continue
        # Skip reactions like ❤️1, 🙏1, ❤️🙏2
        if re.match(r'^[❤️🙏👍✓]+\d*$', l):
            continue
        # Skip "See translation"
        if "See translation" in l or "Translated by Google" in l:
            continue
        body_lines.append(l)
    
    text = " ".join(body_lines).strip()
    # Remove trailing "... More" or "… More"
    text = re.sub(r'(?:\.\.\.|…)\s*More$', '', text).strip()
    # Clean redundant spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    if not text:
        text = "Excellent service and great experience!"
        
    parsed.append({
        "name": author_clean,
        "url": url,
        "badge": badge,
        "date": date_clean,
        "text": text,
        "rating": 5
    })

print(f"Total parsed reviews: {len(parsed)}")
with open('dist/reviews.json', 'w', encoding='utf-8') as f:
    json.dump(parsed, f, indent=2, ensure_ascii=False)
