<!-- PAGE 1 -->
# SJAA EPHEMERIS

## Stardust Adventure
Jim Albers

My Stardust adventure started Dec 15th when I sent an email to SJAA president Mike Koop inquiring about the reentry trajectory to find out where it might be possible to see it. He's participated in many meteor observing campaigns with Peter Jenniskens, of the SETI Institute, and flew on the aircraft to observe the Genesis reentry in Sep, 2004. Amazingly, they had just received their first Stardust Reentry Capsule (SRC) trajectory. He also said that they were looking for some help

to coordinate ground observations as a complement to the planned observations from the DC-8 aircraft. I tentatively agreed, not quite sure what I what signing up to. I exchanged some emails with Mike and Peter, created some finder charts using Skymap for a few locations and made a short presentation at the beginning of the Dec 17th SJAA meeting. Peter and I then talked for most of that meeting about how to get the general public and amateur observers interested in taking photos

and videos. At some point during the meeting, I decided to take on the challenge.

I created a first update of the NASA Ames/SETI Viewing Forum web page the next week. My girlfriend Diana was instrumental in having a web page that had a non-technical introduction and lots of instructions, and didn't immediately go off into topics that only some of us might appreciate. We also contacted the Night Sky Network and Jane Houston Jones to help get the word out to astronomy clubs in the reentry area.

Fortunately I had extra time between Christmas and New Years. I generated a ground track of where the SRC would pass in front of the Moon, as Peter was interested in how the hot wake behind the SRC developed and the Moon would be a good backlight. I learned a lot about the software program I was using to generate the ground track. I was starting to get Viewing Forum Observing Intent emails, some of which included questions and did my best to answer the questions and generate finder charts for those that needed them. I then created my own web page so that all the plots and data that I had been generating could be easily accessible and Peter didn't need to spend so much time away from flight preparations to update his web page. At some point, the idea of using Iridium flares as a test came up as they are very bright transitory events similar to the reentry, so I generated predictions for the nights of the test flights using the Iridflat program. There were flares around 6 p.m. and 6 a.m. every day.

*Continued on page 4*

---

## SJAA Activities Calendar
Jim Van Nuland

### March
**3** Houge Park star party. Sunset 6:04 p.m., 24% moon sets 10:52 p.m. Star party hours: 7:00 to 10:00.

**3** Astronomy Class at Houge Park. 7:30 p.m.

**4** ATM class at Houge Park. 7:30 p.m.

**11 General meeting** at Houge Park. 8 p.m. Paul Zurakowski and Richard Ozer will talk about the Telescope-Maker's workshop at Chabot Observatory in Oakland.

**16** ATM class at Houge Park. 7:30 p.m.

**24** Houge Park star party. Sunset 6:23 p.m., 21% moon rise 4:03 a.m. Star party hours: 7:30 to 10:30

**25** Messier Marathon. Sunset 6:24 p.m., 12% moon rises 6:02 a.m.

### April
**1** Dark sky weekend. Sunset 6:30 p.m., 19% moon sets 10:54 p.m.

**2** DST (Darkness Squandering Time) begins. Advance clock at 2 am -> 3 am.

**7** Houge Park star party. Sunset 7:36 p.m., 77% moon sets 4:37 a.m. Star party hours: 8:30 –11:30 p.m.

**9** Auction XXVI at noon. See article on page 8

**13** ATM Class at Houge Park. 7:30 p.m.

**21** Astronomy Class at Houge Park. 7:30 p.m.

**21** Houge Park star party. Sunset 7:48 p.m., 35% moon rises 3:38 a.m. Star party hours: 9:00 – 12:00 a.m.

**22** Dark sky weekend. Sunset 7:49 p.m., 25% moon rises 4:09 a.m.

**29** Dark sky weekend. Sunset 7:55 p.m., 8% moon sets 10:42 p.m.

*The Board of Directors meets at 6:00 p.m. preceding each general meeting. All are welcome.*

---

## 24 hour news and information hotline: (408) 559-1221
**http://www.sjaa.net**

---

Copyright © 2006 San Jose Astronomical Association, Inc.
**Volume 17 Number 3** Official publication of the San Jose Astronomical Association, March 2006

<!-- PAGE 2 -->
# GPS: Global Positioning on a Shoestring

Bill Maney

How do you figure out where you are on the planet?

These days you can find your address on a mapping website, or maybe switch on a GPS. But before these things what could you do? When I got into astronomy I also started looking at celestial navigation techniques. I got a cheap student sextant (\$35) and a nautical almanac and taught myself how to take a sight and convert it to a line-of-position on a map. With a few lines plotted, I could pinpoint myself within a handful of miles. But it was complicated and I was left asking: If I know what star is right above me, isn't that enough? That same star isn't above any other place on the planet, so that's the only measurement I should need.

So I made an experiment. This is where the shoestring comes in. I lay down on something soft on my driveway and hung a shoestring from a basketball hoop. OK so it was a regular piece of string. I got it wet so that it would hang straighter. I mentally extended the line of the string into the sky and noted the point that it hit and also noted the time. Drops of water got me directly in the eye, so I knew I was well aligned. Then I dragged out my star hopping skills and found the spot on my star chart. The declination of that point is more-or-less the latitude of my driveway. (If I did my math correctly, the non-roundness of the earth causes the measurement to be 5 minutes (≈ 5 nautical miles) lower than my actual latitude).

The right ascension is not my longitude of course because the earth spins. The longitude is given by a formula that I worked out by trial and error using data from www.nao.rl.ac.uk and is not super-accurate (within a half mile or so for 2006) and will probably be pushed into the online version of the newsletter by

my editors. It goes as follows, where Tx is the number of hours since midnight, Jan 1, 2006, Greenwich mean time (subtract 8 hours for the number of hours since midnight PST or 7 hours for PDT), and 6.700555556 was the Right Ascension of the sky over Greenwich at that moment, and Rax is the Right Ascension measurement from the driveway, and Lyear=365.256363, the length of a year, and frac returns the fractional part of a number.

Longitude = 15*(Rax - 6.700555556 - 24*frac(Tx* (Lyear + 1)/Lyear)/24))

Negative numbers are W latitude. If you get a number larger than 180, subtract or add 360. I had to do the experiment a few times to get it right. On the last try, I put in the time to the nearest minute and was only 5 miles off in longitude. Then I corrected it with the time to the nearest second and I was only 1 mile off! This is unbelievable accuracy...literally. That this was pure luck is evidenced by my 3 tries for latitude which were between 15 and 55 miles off. Hey, it's a big planet! And what did you expect for a shoestring!?!

How useful is this? Well... Good luck using it on a rocking boat. And on land, if you don't know where you are within 55 miles, you're pretty lost. The accuracy could be improved by using some magnification instrument. A design using a spinning vat of mercury (highly toxic) is quite appealing (and far from being executed). I'll leave it as an exercise to the reader to determine the point of all this. If you try this technique yourself, the usual warnings about laying down on driveways in the dark apply.

---

# *March General Meeting*

# March 11 General Meeting: Mirror Making and Testing

**Saturday @ 8 p.m.**

David Smith

A telescope mirror must conform to a particular shape very accurately, down to a fraction of a wavelength of light over its whole surface. So it may seem surprising to hear that you can grind and polish your own mirror to these tolerances yourself, by hand, using very simple tools and techniques. Richard Ozer and Paul Zurakowski, of the Chabot Telescope Maker's Workshop (associate director and optical testing guru, respectively), will lead us through the process in our March meeting. They will cover a number of related issues: Why would you want to do it yourself? How is it done? What are you getting yourself into? Why does it work?

The secret of getting a good mirror is the testing and figuring stage, wherein you determine how your mirror surface differs from its desired shape, and correct it. Paul will show us how the Ronchi and slitless testers work, and how to interpret what you see with them. The next step is to use that information to guide your choice of corrective corrective strokes. They will tell us how to do that, but Richard will also show us how to use a computer program to interpret what you see.

The Ronchi and slitless tests are generally considered to be qualitative, not quantitative measurements. But Paul has correlated his results with quantitative measurements from interferometry and the caustic test, and found them to be good to about one-tenth of a wavelength of light, which makes for an excellent mirror.

After the presentation, Paul and Richard will have a mirror and tester set up so that you can get first-hand (first-eyeball?) experience with what you see through the tester, and what that tells you.

---

SJAA EPHEMERIS | Page 2 | March 2006

<!-- PAGE 3 -->
# *The Shallow Sky*

# Which One is the Planet?

Akkana Peck

Mars is still visible high in the evening sky at sunset. It's very small now (its disk is only about twice the size of Uranus') so it will be difficult to see much detail even in a large telescope. Its magnitude is fading fast throughout the month as we recede from it in our faster orbit around the sun; but it's very similar in brightness to that of the nearby red star Aldebaran. At mid-month their magnitudes match exactly. Take a look -- it's a perfect chance to see how well you can tell a star from a planet with the naked eye.

Saturn is high in the sky throughout the prime hours of the evening, and perfectly placed for observing, just a couple of degrees away from the Beehive (M44). The rings are tilted about 20 degrees to us, with the south side showing.

Jupiter rises a few hours before midnight, but it's still quite far south, in Libra, and never gets very high. Of course, there's still plenty to see on the biggest of planets even when it's low in the sky. For instance, moon shadow transits show well even in poor seeing, and there are several double transits worth seeing this month. On March 14th, check out the double satellite/shadow transit (Io and its shadow, plus Ganymede skirting Jupiter's northern edge) starting around 7pm. There's another very similar transit involving the same suspects at 9:30 on the 21st. Then starting around 9:50 on the 28th, Io and Ganymede transit together again, but this time we should see a bit of Ganymede's shadow as well.

Mercury disappears into the sunset

glare early in March, so if you want to observe it, the first few days of the month are your best bet. It will reappear in the morning sky around the end of the month.

Late March is a good time to watch for the zodiacal light in the evening just after the sky first gets dark.

Venus is visible in the morning sky

![New Horizons launched aboard an Atlas V rocket from Cape Canaveral Air Force Station, Florida, on January 19, 2006. Photo courtesy of NASA/JPL-Caltech.](image)

*New Horizons launched aboard an Atlas V rocket from Cape Canaveral Air Force Station, Florida, on January 19, 2006. Photo courtesy of NASA/JPL-Caltech.*

through most of the month. On mornings around the 26-27th, it passes within a couple of degrees of Neptune. They aren't very high, and Neptune would ordinarily be difficult to locate this low in the sky, but you might be able to find it by looking for the dim blue orb two degrees south of Venus and very slightly west.

Uranus is invisible -- too close to the sun. Pluto is trickly, hidden in the morning sky in Ophiuchus, but an ambitious observer might have a chance.

Speaking of Pluto, the New Horizons Pluto mission blasted off successfully on January 19th (after some nail-biting

delays due to weather) and is on its way to Pluto. It won't get there until 2015. Fortunately, the spacecraft launched in time to take advantage of a gravitational slingshot effect from Jupiter as it passes by; if the probe had been delayed a few more weeks, it might have missed Jupiter's help, and wouldn't have gotten to Pluto until 2018, which might have been too late to investigate Pluto's tenuous atmosphere.

Just before the New Horizons launch, Project Stardust came back to us from its mission to Comet Wild 2, floating to a perfect touchdown the Utah desert. Its aerogel collectors are full of particles from the comet, and should keep mission scientists busy for years to come. And you can help: they've put the call out to volunteers to help analyze the particles. The goal is to find grains of interstellar dust mixed in with the pieces of comet

debris. You can use a web application (no special software needed) to look at microscope images of the particles, and try to recognize those that came from outside the solar system. There's more information at: http:// stardustathome.ssl.berkeley.edu/

We'll just miss the penumbral lunar eclipse on March 14: it ends just before the moon rises here, but if you happen to be visiting more easterly states on that night, check it out. We also miss the companion solar eclipse, on the 29th, but let's hope that the SJAA folks who are traveling to see it have a nice show and bring back pictures and stories for the rest of us.

and other solar system

---

SJAA EPHEMERIS | Page 3 | March 2006

<!-- PAGE 4 -->
# Stardust Adventures
*Continued from page 1*

After the New Year, the team wanted an independent analysis of the aircraft observing conditions to have the highest probability of observing the reentry, so I started working with Dean Kontinos of NASA Ames to analyze alternate aircraft viewing locations in case of cirrus clouds and variations in the reentry trajectory.

A news conference was scheduled for Jan 11th, at NASA Ames and we were also planning to have a meeting of the ground observers. Journalists were invited to apply to fly on the rehearsal flights or the reentry flight. I applied as a reporter for the SJAA Ephemeris and for my company newsletter, but never received a response. There was a good turnout of TV, radio and print journalists at the news conference, and I talked to a number of them about getting the general public to observe the reentry and gave them handouts with our URL. Ron Dantowitz and Marek Kozubal from the Clay Center Observatory were also there with their automated tracking telescope. Peter Jenniskens was very busy with the journalists and helping prepare for the flight.

After many of the journalists left, I went into the DC-8 observing aircraft to look around. On both sides of the aircraft are several rows of large comfortable seats alternated with storage boxes, bolted down equipment, and clear areas with instrument mounts on the windows. I was asked to update the aircraft navigator for the time and location of the Iridium flare. It suddenly occurred to me that a planeload of people were all going to be depending on my predictions being correct. Peter was going to give the printouts back to me, and I said he should just keep them unless I was going on the flight. He then surprised me by saying that one of the investigators wasn't going, I had applied for a flight and had been helping out, so I was welcome to come along!

Suddenly I had to go to safety and flight briefings and needed to fill out a "next of kin" form. At the flight briefing, Peter introduced me as the person to thank if the Iridium flare took place as predicted and the person to blame if it didn't. It was quite an introduction to the group. I then rushed off to pick up a few things from home and grab some food for the plane, as I had never had time for lunch. When I returned, a flightsuit was found and I quickly put it on before the doors were shut and we had to be in our seats. Everyone had headsets to help keep the plane noise to a minimum and so that everyone could communicate.

**"Peter ... surprised me by saying that one of the investigators wasn't going..., so I was welcome to come along!"**

captured the flare and watched some video of it taken by one of the cameras.

We then started a "racetrack" pattern over the Pacific off the central coast of California. The pattern had two straight sides and two 180 degree turns so that the instruments could be aligned and checked

out and the operators could get experience pointing them at stars and the Moon. I went around the cabin trying to watch what was going on and stay out of the way.

We took off at 5 p.m. to the North and gained altitude over the Bay Area, as the sun was setting through scattered clouds. The view out the window was quite nice. I finally got to eat my lunch as each of the groups responsible for a given instrument were cleared to setup and start checking their equipment one by one. Everything had to be packed up in the large storage boxes for takeoff and landing, and then looked at by a member of the flight crew after it had been setup. After a while, the cabin lights were turned out. It was darker than before, but it certainly wasn't like amateur observing from a dark site as the cabin was filled with bright video monitors and computer screens. That's modern astronomy.

Everyone was pretty much ready before the Iridium flare over Monterey at 6:02 p.m. We got some notification of it occurring, but I had to take off my headset in order to look out the window on the opposite side of the aircraft. I watched the time indicator on my GPS and waited. Right on time, the flare showed up where predicted, thank goodness. I then walked around a bit and found that most instruments had

One of the first things the team learned on this first test flight in the cold air at 39,000 ft. was that the air tubes that kept the windows from fogging up needed to be reoriented. Most teams solved this problem by adjusting the tubes themselves, but a couple would require further adjustment after the flight. I helped a bit by loaning out my flashlight for most of the flight, and Mike Koop and I pointed out stars and constellations to the astronomers just like at a star party. Mike let me put on the video goggles he used for pointing the Eschelle spectrometer. I practiced tracking stars and kept an eye on the computer monitor to see if I was actually tracking well enough to capture spectra. It wasn't easy when the target was moving due to the plane turning, turbulence, etc. You're down on your knees, and the instrument gets heavy after a while. I was glad I didn't have to be the one following the SRC as it went by.

Pretty soon it was time to pack everything up for landing. The light sensitive instruments were shut down, the cabin lights were turned back on, everything was put back into the storage boxes, and we strapped back into our seats. A flight briefing was held as we headed back home. Not everything was perfect, but it was a

---

SJAA EPHEMERIS Page 4 March 2006

<!-- PAGE 5 -->
successful first rehearsal. We landed
back at Moffett after being in the air for
3 hours, and I headed home. It's the
only time I've ever been happy about
returning to the same airport after
flying around for 3 hours. Some of the
scientists were planning to come back
and work after a short dinner break.

My friend Bryan and I wanted to be in
Eastern Nevada to see the brightest part
of the trajectory, but

the weather was
starting to look like
it wasn't going to
cooperate. We
ended up driving to
Reno on Friday and
then back over the
Sierra Nevada
Mountains in the
snowstorm on
Saturday to observe
the reentry from
Redding. Thanks to
my girlfriend Diana
working as our
informal travel
agent, we stayed in
hotels that were easy
to get the
equipment in and
out of and had
Internet access. That
way I could

continue helping with the analysis to
account for changes in the trajectory
due to the last couple of maneuvers and
we could watch the weather.

It was cloudy in Redding when we
arrived and we couldn't really find a very
good site after driving around for a
while. After dinner it even started to
rain slightly, so I was thinking we could
always watch the reentry on NASA TV
on the Web. I actually did have some
faith in the weather predictions, and
sure enough, about 8:30 I went outside
to check and saw the Moon and a
virtually cloud free sky full of stars, so
felt very relieved and Bryan and I were
able to take some test stills and video.

On the way to our observing sight, we

came upon a clearing on the side of the
road up on a hill with a good view to
the North and NE, so we setup there.
We had WWV reception for a while but
then it dropped out, so I had to keep
watching the GPS to keep track of time,
which at 2 AM after driving for 2 days, I
didn't do very well. We were both
watching to the NW of Polaris, hoping
to see the SRC as soon as possible.
Fortunately Bryan noticed it as it

watched the recovery, got a few hours
sleep and drove home. While our
personal observing had not gone as well
as it could have, I was pleased that I had
made a valuable contribution to the
Stardust reentry observing campaign.

Since then we've received a number of
photos and videos from our observers
and I've gotten copies of some of the
video from the aircraft and

![Image of a large group of people in blue uniforms standing in front of a white aircraft labeled "UNITED STATES OF AMERICA"]

appeared just East of Polaris, and we
quickly swung our cameras over to
follow it. I was able to get about 20
seconds of video on 2 cameras and
Bryan took a number of digital stills. We
were able to follow it down to just a few
degrees above the horizon, where it
disappeared into the clouds. This was
surprising as most of the brightness was
expected to be due to heating on the
front of the SRC and by that point we
were pretty much looking at the back
of it and through a whole lot of
atmosphere. More recent photometric
analysis of the video confirmed our
impression of the brightness over time
that night.

We went back to the hotel, Diana
helped me get a number of the
observations posted to the Web,

have done
some more
analysis. I've
been digitizing
the videos,
creating light
curves from
the video
frames and
learning a lot
about video
CODECs. I've
also been
registering long
exposure
photos with
the trajectory
and stars so
that light
curves can be
derived from
the photos.
Both are also

being analyzed to compare SRC
position to predictions. It continues to
be an engaging and challenging project
that fills my free time.

My Stardust Web Page: http://
dgilbert3.home.mindspring.com/
stardust.htm

Photos of the DC-8 aircraft the day of
my test flight taken by Bryan
Murahashi: http://www.pbase.com/
bryan_murahashi/
jan_11__dc8_airborne_laboratory

Peter Jennisksen's Reentry page: http://
reentry.arc.nasa.gov/index.html

The Viewingforum page that I updated:
http://reentry.arc.nasa.gov/
viewingforum.html

---

SJAA EPHEMERIS Page 5 March 2006

<!-- PAGE 6 -->
# NASA Space Place

## Micro-sats with Macro-potential
Patrick L. Barry

Future space telescopes might not consist of a single satellite such as Hubble, but a constellation of dozens or even hundreds of small satellites, or "micro-sats," operating in unison.

Such a swarm of little satellites could act as one enormous telescope with a mirror as large as the entire constellation, just as arrays of Earth-bound radio telescopes do. It could also last for a long time, because damage to one micro-sat wouldn't ruin the whole space telescope; the rest of the swarm could continue as if nothing had happened.

And that's just one example of the cool things that micro-sats could do. Plus, micro-sats are simply smaller and lighter than normal satellites, so they're much cheaper to launch into space.

In February, NASA plans to launch its first experimental micro-sat mission, called Space Technology 5. As part of the New Millennium Program, ST5 will test out the crucial technologies needed for micro-sats—such as miniature thrust and guidance systems—so that future missions can use those technologies dependably.

Measuring only 53 centimeters (20

inches) across and weighing a mere 25 kilograms (55 pounds), each of the three micro-sats for ST5 resembles a small television in size and weight. Normal satellites can be as large and heavy as a school bus.

"ST5 will also gather scientific data, helping scientists explore Earth's magnetic field and space weather," says James Slavin, Project Scientist for ST5.

![Image showing three micro-satellites in space with Earth visible in the background]

Slavin suggests some other potential uses for micro-sats:

A cluster of micro-sats between the Earth and the Sun—spread out in space like little sensor buoys floating in the ocean—could sample incoming waves of high-speed particles from an erupting solar flare, thus giving scientists hours of warning of the threat

posed to city power grids and communications satellites.

Or perhaps a string of micro-sats, flying single file in low-Earth orbit, could take a series of snapshots of violent thunderstorms as each micro-sat in the "train" passes over the storm. This technology would combine the continuous large-scale storm monitoring of geosynchronous weather satellites—which orbit far from the Earth at about 36,000 kilometers' altitude—with the up-close, highly detailed view of satellites only 400 kilometers overhead.

If ST5 is successful, these little satellites could end up playing a big role in future exploration.

The ST5 Web site at nmp.jpl.nasa.gov/ st5 has the details. Kids can have fun with ST5 at spaceplace.nasa.gov, by just typing ST5 in the site's Find It field.

*This article was provided by the Jet Propulsion Laboratory, California Institute of Technology, under a contract with the National Aeronautics and Space Administration.*

SJAA EPHEMERIS | Page 6 | March 2006

<!-- PAGE 7 -->
# 2006 Messier Marathon

Bob Havner

The San Jose Astronomical Association will be hosting the 2006 Messier marathon on March 25/26 at Henry Coe State Park. The Messier marathon as an attempt to find 109 of the Messier objects in one night! French comet hunter Charles Messier created the catalog to identify objects that could be mistaken for comets. Today's list represents 110 of the most famous deep sky objects in the night sky. While being a favorite goal of amateur astronomers to complete over time, late March offers an opportunity to find 109 of the Messier objects in a single night.

Don Machholz brought the Messier marathon to the SJAA with an article titled "Messier marathon" in the September 1978 SJAA newsletter. In the article, he invited members to join him on Loma Prieta mountain in March for the event. Using star atlases, a planisphere, and his own comet hunting records, Don developed the observing order, or search sequence, the same list used by most marathoners to this day.

The first San Jose Astronomical Association Messier marathons were held on the nights of March 23/24, 24/25, 30/31 and March 31/April 1, 1979. About fifty club members turned out at these events. Of those, about a dozen participated in the actual marathon. On March 30/31 Don Machholz and Gerry Rattley found 108 objects each, missing only M74 and M33! Amazingly on the night of March 12/13 1980 Don successfully found all 109 objects without star charts, relying only on search instructions he previously recorded on cassette tapes!

The 2006 Messier marathon will be held at the overflow parking area at Henry Coe. Directions can be found at the SJAA website http://www.sjaa.net/

directions.html. Although not required, we recommend pairing up with someone as a way of verifying observations. Observing lists will be available at the site. There will be 3 lists: a short list of bright, easy to find objects for novice astronomers, a half list for those who would rather not make it an all nighter, and the long list for you diehard marathoners.

> *As in past years, if the forecast for Saturday looks much worse than Friday's, expect many people to attempt the Messier Marathon on Friday, March 24/25. Check http://koopm.best.vwh.net/messier.html for weather updates or cancellation.*

There are two books written by SJAA members on the subject of the Messier marathon. Don Machholz's booklet, The Messier Marathon Observer's Guide, gives a detailed search sequence, finder charts, and star hopping information. It also points out that less complete Messier marathons may be run at every time in the year. Robert Garfinkle's book, Star-Hopping: Your Visa to Viewing the Universe (Cambridge University Press, 1994, 1997) has a chapter with instructions and the list for doing a Messier marathon. Copies of Don Machholz's The Messier Marathon Observer's Guide will be for sale at the March 11 general meeting and at the marathon (while supplies last) for $10.00.

Also check out the SEDS Messier page http://www.seds.org/messier/xtra/marathon/marathon.html. They have many helpful links to images and lists.

You will want to have a planisphere and a good star atlas, preferably plastic or plastic coated, to locate constellations and for star hopping to the objects. As always, come prepared for cold weather and a long night; bring plenty of warm clothing and hot drinks.

This is a great time for those that are new to astronomy to be introduced to the deep sky. Don't expect to get them all if this is your first time, just have a good time and enjoy the ones you do find. You will get a good start on completing your own Messier list.

Come out to Henry Coe with us for a night of astronomy and start (or perhaps finish) your Messier list.

Messier marathon Henry Coe State Park. March 25, 2006 There is a $5.00 per vehicle night use fee or a $12 fee if you use a campsite.

## Directions to Houge Park

Houge (rhymes with "Yogi") Park is in San Jose, near Campbell and Los Gatos. From Hwy. 17, take the Camden Avenue exit. Go east 0.4 miles, and turn right at the light, onto Bascom Avenue. At the next light, turn left onto Woodard Road. At the first stop sign, turn right onto Twilight Drive. Go three blocks, cross Sunrise Drive, then turn left into the park.

From Hwy. 85, take the Bascom Avenue exit. Go north, and turn right at the first traffic light, onto White Oaks Road. At the first stop sign, turn left onto Twilight Drive. You will now be passing the park. Turn right at the first driveway, into the parking lot.

---

SJAA EPHEMERIS &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Page 7 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; March 2006

<!-- PAGE 8 -->
# Auction XXVI

Mike Koop

It's spring, and time for the annual migration of astronomical paraphernalia from one garage to another! On Sunday, April 9, 2006, an astronomical auction and swap meet will be conducted at Houge Park in San Jose, sponsored by the San Jose Astronomical Association. The SJAA Auction is a great opportunity for beginners to purchase their first telescope at a great price! Experienced observers often find equipment they need for their next observing project, from Olll filters to finders to star charts. All kinds of interesting items are found in the auction.

It's an even year, so Kevin Medlock will be our auctioneer. Those who have observed his performance in previous auctions have learned to appreciate his skillful evaluation of classical astronomical items on the spot. Great entertainment for all!

Doors open at 11:30 am to register material for the auction. All material must be registered by 12:30 p.m. to allow sufficient time to enter the items into the computer and to allow bidders time to view the auction material. Over the years, we have discovered that the maximum number of items that we can sell before the audience gets restless is about 100. Please limit yourself to four items maximum for the auction. In order to reserve your spot in the

auction, please preregister your items so that people know what you are bringing as described below. The club reserves the right to accept only appropriate material for the auction.

The auction will begin at 1 p.m., and will run as long as needed. Seller may specify a minimum bid, which if not met, will return the item back to the seller with no commission applied. After the auction, buyers and sellers settle up using one check to (or from) SJAA and claim their items. Seller pays 10% commission, with a cap of $50 for any one item. We do not handle charge cards. There is no fee for bidder cards.

After the auction, material for the swap meet will be allowed into the hall, about 3 p.m The swap also allows people some additional haggling time for those items that were optimistically priced by the seller in the auction, or to sell those odds and ends items which were better off being in a swap, or turned away due to the 100 item auction limit. Sellers are encouraged to bring items that would interest the astronomical audience such as astronomical, science, computer, or tech items. Joe Sunseri of Earth and Sky Adventure Products will be there with many fine new and used items, including eyepieces, finders, and binoculars. At the swap, each buyer pays the seller. Sellers are to keep track of their sales, and pay a 10%

commission, as for the auction. There are no table fees. All commissions from the auction and the swap are tax-deductible, as SJAA is a 501(c)(3)educational organization.

The SJAA offers free advertising if you preregister your items for the auction. Please email the auction team at auction@sjaa.net with a description of the item and a picture if possible. All items submitted by 6 PM on Saturday, April 8th will be added to the auction website. This allows the bidders to find out how much that APO scope is really worth, so you will be more likely to sell it.

Part of running a successful auction is to make sure that there are people who are new to astronomy in attendance. We can use your help to make this so! Go to the auction website linked off the main page, download, and print a auction poster to display. Post them at the bulletin boards at work, at church, at your local library, or where you think people might be interested. Hand it out to a friend who has expressed interest in getting a telescope. You get the idea! Thanks for your assistance!

For more about SJAA, visit our web site at http://www.sjaa.net or email to the above address. See you there!

Directions to Hogue Park are on page 7.

# SJAA Yosemite Public Star Party 2006

Jim Van Nuland

The annual SJAA Yosemite star party will be held on July 21 and 22, at Glacier Point in Yosemite National Park. Up to 30 people will be given free admission and camping, in exchange for two public events on Friday and Saturday evenings. The rest of the time we can be tourists.

We are expected to have at least one

scope per two people, and to attend both star parties.

The camping is rough by modern standards: no dining room, no showers, no hot water. Read about it on my Yosemite page at <http://www.svpal.org/~jvn/yosemite.htm>, or contact me with questions. If you can

tolerate the limitations, tell me the number of people you'll have, and the number of scopes that will be set up for the public. E-mail me at jvn@svpal.org, or phone 408-371-1307 10 a.m. to 10 p.m. Priority is given to SJAA members.

The new moon is on July 23, so this is an ideal date.

---

SJAA EPHEMERIS | Page 8 | March 2006

<!-- PAGE 9 -->
# Board of Directors Elected

At the February 11 general meeting, the Board of Directors was elected for the coming year. Four directors are elected in even-numbered years; five in odd years.

Standing for re-election were Gary Mitchell, Dave Smith, Mike Koop, and Rob Hawley. No candidates were nominated from the floor, so the membership voted to close nominations and declare the candidates elected.

At the previous board meeting, directors Jim Van Nuland and Dana Crom resigned, each at mid-term. Appointed to fill their terms were Dr. Lee Hoglan and Rich Neuschaefer, respectively. Craig Scull was appointed Secretary. Craig and Bill O'Shaughnessy have a year remaining on their terms.

The SJAA thanks Jim and Dana for their years of service to the SJAA. Jim has been on the board of directors since 1973 and secretary since 1979. Jim said that he is not leaving the club, but wanted to make room on the Board for someone who can better address the club's business and goals. He will continue coordinating the school star party program. Dana has been on the board of directors since 2003. He resigned due to increasing work load with frequent trips to Korea. Dana hopes to volunteer where needed when he is in town.

# Physics for Poets

Andrew Fraknoi

Last year, Foothill College's "Physics for Poets" class won the 2005 Innovation of the Year Award from the League for Innovation in the Community Colleges, for finding new ways to explain Einstein's ideas without math. This spring, instructor Andrew Fraknoi is offering this course again, and the college invites everyone with an interest in Einstein and his strange ideas to come and check it out.

Numbered Physics 12 in the Foothill catalog, "Physics for Poets: Everything You Wanted to Know about Einstein's Work but Were Afraid to Ask", will be offered on Tuesday and Thursday evenings from 6 to 8:30 p.m., April 11 to June 22, 2006.

The non-technical course introduces students to some of the most intriguing areas of modern physics, with a focus on Einstein's contributions. The approach uses humor, analogies, and demonstrations. No background in science or math will be required; the

instructor specializes in explaining scientific ideas in everyday language.

The course emphasizes key ideas that form the basis of our modern concepts of space, time, matter, and energy:

* The theory of how atoms work
* Energy, heat, and the arrow of time
* The special theory of relativity: what happens when you travel close to the speed of light
* The general theory of relativity: gravity, space-time warps, and black holes
* Quantum mechanics: the bizarre rules that govern the world inside the atom

For registration information for the Spring Quarter at Foothill College in Los Altos, see: http://www.foothill.edu/reg/ spring06.html

For a course syllabus in pdf format, see: http://www.foothill.edu/psme/ Physics.12.Web.pdf

# EAS Awards JVN on March 12th

Mike Koop

Eastbay Astronomical Society will award Jim Van Nuland the Helen Pillans Award for 2006. This prestigious award is given to an individual or institution that has meritoriously served the amateur astronomy community. The award was first given to Helen Pillans, a popular faculty member at Mills College and Amateur Telescope Maker. Jim is recognized by the EAS for his direction of the SJAA school star party program over the last 20 years. Starting in the late Eighties, Jim and other SJAA members had an informal group which would go to local schools and set up their telescopes. Through word of mouth, other teachers started making requests for visits by the astronomers. In response to all the increasing requests, the board officially appointed Jim the School Star Party Chairman in November of 1996. Since then, Jim has meticulously scheduled, provided direction to, and notified members about the events. His van often is the marker used to show where to set up the scopes. It is the primary outreach effort done by the SJAA. Last year, there were over 60 events scheduled by Jim which were attended by over 10 thousand students through out Santa Clara County and the bay area! Previous Pillan Award winners include SJAA Members Jane Houston Jones and both Kevin and Denni Medlock.

The Helen Pillans Award is the highlight of the annual EAS Banquet. It is held at the Chabot Space and Science Center on Sunday March 12th. Doors open at 5:45, with dinner served at 6:30. The guest speaker this year is Nobel Laureate Dr. Charles H. Townes, on the subject of "The Parallelism and Eventual Convergence of Science and Religion." All SJAA Members, friends, and family are invited to attend. The cost is $33 per person. Go to the EAS website to sign up. (http://www.eastbayastro.org/) Congratulations Jim on your well deserved award!

---

SJAA EPHEMERIS Page 9 March 2006

<!-- PAGE 10 -->
# Silicon Valley Astronomy Lecture Series

# Scott Sandford to talk on March 1, 2006 at 7 p.m.

Andrew Fraknoi

Dr. Scott Sandford from NASA Ames will give a non-technical illustrated talk on Project Stardust – the comet studying spacecraft that made a successful landing in Utah on January 15. This talk will be at 7 p.m. on Wednesday, March 1. It will be in the Smithwick Theater, Foothill College, El Monte Road and Freeway 280, in Los Altos Hills, California. This event is free and open to the public. Parking is $2 at Foothill College. Call the series hot-line at (650) 949-7888 for more information.

The Stardust mission is a spacecraft that flew by and, for the first time ever, collected samples from a comet (Comet Wild-2.) The samples were successfully returned to Earth on January 15, 2006 and are now being analyzed. The spacecraft traveled about 2.9 billion miles over 7 years to collect and bring back samples of what may be some of the earliest material from the solar system ever seen.

Dr. Sandford, an expert on meteorites and the material between the planets, is co-investigator on the Stardust mission, and was actively involved in the recovery of the Stardust capsule in the Utah desert. He will fill us in on what this historic mission accomplished and what the initial analysis of the samples is revealing.

The series is co-sponsored by NASA Ames Research Center, Foothill College Astronomy Program, SETI Institute, and the Astronomical Society of Pacific.

---

# Solar System Stats for March 2006

Adapted from the Observer's Handbook published by The Royal Astronomical Society of Canada which in turn gets this data from the U.S. Naval Observatory's Nautical Almanac Office and Her Majesty's Nautical Almanac Office and contributions by David Lane, St. Mary's University, Halifax NS.

|          |    | Mercury   | Venus     | Mars      | Jupiter   | Saturn    | Uranus    | Neptune   | Sun       |
|----------|----|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------| 
| RA       | 1  | 23h43m    | 19h51m    | 4h13m     | 15h07m    | 8h32m     | 22h50m    | 21h22m    | 22h47m    |
|          | 11 | 23h26m    | 20h24m    | 4h36m     | 15h06m    | 8h30m     | 22h52m    | 21h24m    | 23h24m    |
|          | 21 | 22h59m    | 21h02m    | 5h00m     | 15h05m    | 8h28m     | 22h54m    | 21h25m    | 0h01m     |
| Dec.     | 1  | 0°58'     | -16°18'   | 22°59'    | -16°12'   | 19°37'    | -8°16'    | -15°35'   | -7°45'    |
|          | 11 | 0°18'     | -15°48'   | 23°49'    | -16°10'   | 19°45'    | -8°03'    | -15°28'   | -3°53'    |
|          | 21 | -4°30'    | -14°33'   | 24°28'    | -16°03'   | 19°51'    | -7°50'    | -15°23'   | 0°04'     |
| Dist (AU)| 1  | 0.80      | 0.49      | 1.34      | 4.99      | 8.29      | 21.07     | 30.97     | 0.991     |
|          | 11 | 0.63      | 0.57      | 1.44      | 4.85      | 8.39      | 21.06     | 30.90     | 0.993     |
|          | 21 | 0.64      | 0.65      | 1.54      | 4.71      | 8.52      | 21.02     | 30.80     | 0.996     |
| Mag      | 1  | 0.5       | -4.5      | 0.7       | -2.2      | -0.1      | 5.9       | 8.0       |           |
|          | 11 | 5.2       | -4.4      | 0.9       | -2.3      | 0.0       | 5.9       | 8.0       |           |
|          | 21 | 2.2       | -4.3      | 1.1       | -2.3      | 0.0       | 5.9       | 8.0       |           |
| Size     | 1  | 8.4"      | 33.8"     | 7.0"      | 39.5"     | 20.1"     | 3.3"      | 2.2"      | 32'17"    |
|          | 11 | 10.7"     | 29.4"     | 6.5"      | 40.7"     | 19.8"     | 3.3"      | 2.2"      | 32'12"    |
|          | 21 | 10.6"     | 25.8"     | 6.1"      | 41.8"     | 19.5"     | 3.3"      | 2.2"      | 32'07"    |

---

SJAA EPHEMERIS                                    Page 10                                    March 2006

<!-- PAGE 11 -->
# Officers and Board of Directors

**Pres** Mike Koop (408) 446-0310  
**VP** Rob Hawley (408) 997-6526  
**Sec** Craig Scull (408) 292-9317  
**Tres** Gary Mitchell (408) 265-2336  
**Dir** Bill O'Shaughnessy  
(408) 984-8304  
**Dir** David Smith (408) 978-5503  
**Dir** Rich Neuschaefer  
**Dir** Lee Hoglan  
**Dir** Gordon Reade

## *Ephemeris Staff*

**Editors** Paul & Mary Kohlmiller  
(408) 848-9701

**Circulation**  
Bob Brauer (408) 292-7695  
Lew Kurtz (408) 739-7106  
Dave North north@znet.com  
**Printing** Accuprint (408) 287-7200

## *School Star Party Chairman*
Jim Van Nuland (408) 371-1307

## *Telescope Loaner Program*
Mike Koop (408) 446-0310

## *Web Page*
Paul Kohlmiller pkohlmil@best.com

## *SJAA Email Addresses*

Board of Directors board@sjaa.net  
Membership ?s membership@sjaa.net  
Chat List chat@sjaa.net  
Ephemeris ephemeris@sjaa.net  
Circulation circulation@sjaa.net  
Telescope Loaners loaner@sjaa.net  
Members Email Lists:  
http://www.sjaa.net/mailman/listinfo

## Publication Statement
SJAA Ephemeris, newsletter of the San Jose Astronomical Association, is published monthly.

San Jose Astronomical Association,  
P.O. Box 28243  
San Jose, CA 95159-8243

## Submit
Submit articles for publication in the SJAA Ephemeris. Send articles to the editors via e-mail to ephemeris@sjaa.net. **Deadline, 10th of previous month.**

---

# SJAA loaner scope status

All scopes are available to any SJAA member; contact Mike Koop by email (koopm@best.com) or by phone at work (408) 473-6315 or home (408) 446-0310 (Please leave message, phone screened).

## Available scopes

These are scopes that are available for immediate loan, stored at other SJAA members homes. If you are interested in borrowing one of these scopes, please contact Mike Koop for a scope pick up at any of the listed SJAA events.

| # Scope | Description | Stored by |
|---------|-------------|-----------|
| 1 | 4.5" Newt/ P Mount | Annette Reyes |
| 3 | 4" Quantum S/C | Hsin I. Huang |
| 6 | 8" Celestron S/C | Karthik Ramamurthy |
| 7 | 12.5" Dobson | Tom Fredrickson |
| 8 | 14" Dobson | Colm McGinley |
| 10 | Star Spectroscope | Jim Albers |
| 11 | Orion XT6 Dob | Ravi Shankar Erram |
| 14 | 8" f/8.5 Dob | Colm McGinley |
| 15 | 8" f/9 Dobson | Mike Koop |
| 19 | 6" Newt/P Mount | Daryn Baker |
| 23 | 6" Newt/P Mount | Wei Cheng |
| 24 | 60mm Refractor | Al Kestler |
| 26 | 11" Dobson | Vivek Kumar |
| 27 | 13" Dobson | Steve Houlihan |
| 28 | 13" Dobson | Anupam Dalal |
| 29 | C8, Astrophotography | Mark Ziebarth |
| 32 | 6" f/7 Dobson | Sandy Mohan |
| 33 | 10" Deep Space Explorer | Jack Zeiders |
| 34 | Dynamax 8" S/C | Yuan-Tung Chin |
| 36 | Celestron 8" f/6 Skyhopper | Charles Santori |
| 38 | Meade 4.5" Digital Newt | Tej Kohli |
| 39 | 17" Dobson | Steve Nelson |
| 41 | 18" Sky Designs Dob | Len Bradley |
| 42 | 11x80 Binoculars | Ritesh Vishwakarma |
| 43 | Orion XT4.5 Dob | Gary Mitchell |

## Scope loans

These are scopes that have been recently loaned out. If you are interested in borrowing one of these scopes, you will be placed on the waiting list until the scope becomes available after the due date.

| # Scope | Description | Borrower | Due Date |
|---------|-------------|----------|----------|
| 12 | Orion XT8 Dob | Judy Arauz | 3/17/06 |
| 35 | Meade 8" Equatorial | Mike Horzewski | 4/20/06 |
| 37 | 4" Fluorite Refractor | Peter Young | 5/11/06 |
| 40 | Super C8+ | Bill Kerns | 4/20/06 |
| 44 | 4.5" Skyview/ P Mount | Mantle Yu | 5/03/06 |

## Extended scope loans

These are scopes that have had their loan period extended. If you are interested in borrowing one of these scopes, we will contact the current borrower and try to work out a reasonable transfer time for both parties.

| # Scope | Description | Borrower | Due Date |
|---------|-------------|----------|----------|
| 2 | 6" f/9 Dob | John Paul De Silva | ? |
| 9 | C-11 Compustar | Bill Maney | Indefinite |
| 13 | Orion XT6 Dob | Rajiv Vora | 04/20/06 |
| 16 | Solar Scope | Ken Frank | 05/13/06 |
| 21 | 10" Dobson | Michael Dajewski | Repair |

## Waiting list:
(lots of scopes available!!!)

---

SJAA EPHEMERIS Page 11 March 2006

<!-- PAGE 12 -->
# San Jose Astronomical Association Membership Form

*You can join or renew with the SJAA online at http://www.sjaa.net/SJAAmembership.html*

☐ **New** ☐ **Renewal** (Name only, plus corrections below)

**Membership Type:**
- ☐ Regular — $20
- ☐ Regular with Sky & Telescope — $53
- ☐ Junior (under 18) — $10
- ☐ Junior with Sky & Telescope — $43

Subscribing to Sky & Telescope magazine through the SJAA saves you $10 off the regular rate. (S&T will not accept multi-year subscriptions through the club program. Allow 2 months lead time.)

Bring this form to any SJAA Meeting or send (with your check) to

**San Jose Astronomical Association**  
**P.O. Box 28243**  
**San Jose, CA 95159-8243**

Make your check payable to "SJAA"  
*(not Sky Publishing)*

**Name:** _______________________________________________________________

**Address:** _______________________________________________________________

**City/ST/Zip:** _______________________________________________________________

**Phone:** _______________________________________________________________

**E-mail address:** _______________________________________________________________

---

San Jose Astronomical Association  
P.O. Box 28243  
San Jose, CA 95159-8243

Nonprofit Organization  
U.S. Postage Paid  
San Jose, California  
Permit No. 5381

---

**SJAA EPHEMERIS** Page 12 **March 2006**