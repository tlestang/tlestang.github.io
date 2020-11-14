Title: Projects
Date: 2020-10-04 13:40
Summary: A list of past and current projects

As a Researcher Software Engineer I take part in [various research
software projects](#current-software-projects) and deliver [training
courses](#courses). As much as I can, [I'm getting
involved](#community) with both the local academic community at
Oxford and the wider, global research software engineering movement.

# <a name="current-software-projects"></a> Current software projects

## PyBaMM

Design and manufacturing of more efficient and resilient energy
storage solutions is a key effort towards the development of
sustainable energy systems. Beyond our laptops and phones, batteries
allow the storage of energy from fluctuating renewable energy sources
such as wind-farms.  Increasingly, electricity-powered vehicles are
becoming reality, from cars all the way to small planes!

[PyBaMM](https://www.pybamm.org/) is a python package for designing,
simulating and analysing battery models. Development started in 2019
at the Mathematical Institute (University of Oxford) and the project
was soon adopted as the common modelling framework for the Faraday
Institution, the main entity supporting battery research in the
UK. Battery models are traditionally solved using multi-scale
modelling software such as COMSOL. In contrast, PyBaMM is a free (as
in freedom) package available to all for use but also to contribute
to. Beyond efficiently solving battery models, PyBaMM aims at becoming
a community tool, developed by and for battery scientist.

## stochare

Stochastic models (understand mathematical models of random processes)
arise in many scientific fields: physics, chemistry, biology,
finance... [Stochrare](https://github.com/cbherbert/stochrare) aims at
providing a toolbox to support research dealing with stochastic
processes regardless of the application domain. For instance:

- numerical integration of SDEs
- numerical solver for the Fokker-Planck equations
- first-passage time computation
- instanton computation
- rare event algorithms


Although the package was initially developed with an
out-of-equilibrium statistical physics point of view, it aims at
providing tools to support research with stochastic processes in any
of these fields.

# Past software projects

## Oxford Visual Perception Screen (OxVPS)

A large number of stroke patients - up to almost 80% - suffer visual
impairment after stroke. Such impairment can include neglecting
objects on one side of vision, visual hallucinations, difficulties
recognising faces or objects and impaired motion perception. Only 20%
of patients and carers, however, self-report these impairments and
systematic screening is therefore essential.

Together with Fergus Cooper and Mihaela Duta, we teamed up with Dr
Kathleen Van Cleef (Experimental Psychology, University Of Oxford) to
turn a previously developed paper based assessment into a full-blown
mobile app. And app can be used by clinicians in Acute Stroke Units
with very limited time and provide automated assessment scoring and reporting
of the results.

The app was developed in typescript using the ionic cross-platform
framework, and primarily targets Android tablets. A number of specific
development challenges had to be addressed, including:

- ensuring that the app is suitable for stroke patients who have
  impairments such as neglecting objects on one side or difficulties
  recognising objects;
- ensuring all possibly tablet functionality, other than intended
  interaction sites, is locked down while participants are interacting
  with the tablets;
- ensuring all data is handled in an appropriately secure manner.

We also implemented an automatic scoring system, with a results
overview being automatically generated at the end of each assessment
for the benefit of the clinician performing the screening. More
complete data is securely stored in a cloud database, and can be
downloaded for additional processing by Dr Vancleef and her team.

## smif

Infrastructure systems (think water and energy supply, transport
systems...) provide essential basic services to society but can also
have harmful social and environmental impacts. Plans and decisions are
subject to uncertain socio-economic, technological and environmental
change and these complexities are best studied through simulation.
[smif](https://github.com/nismod/smif)[1,2] is a software framework
for the integration of simulation models of infrastructure systems
such as energy, transport, water and digital communications.

Smif enables the coupling and orchestration of an heterogeneous
ensemble of models: each model has its own space and time resolution,
set of inputs and outputs and data formats. To run under smif, models
must be wrapped by a well-defined Python class, which provides a
common interface. Smif’s purpose is to provide infrastructure systems
modellers a tool capable of handling the execution of the models
according to their dependencies, as well as the necessary data
exchange between models, transforming data if necessary.

The development of smif is driven by the [National Infrastructure
Systems Model (NISMOD2)](https://github.com/nismod/nismod2), which
consists of a collection of high-resolution infrastructure models of
the United Kingdom. However, smif is a very general framework that can
applied whenever models can be executed from Python, via import,
binding, or call out to a command-line executable.

1. Will Usher and Tom Russell | **A Software Framework for the
   Integration of Infrastructure Simulation Models** | [*Journal of
   Open Research Software*](https://openresearchsoftware.metajnl.com/)
   | 2019 | ([doi](https://doi.org/10.5334/jors.265))

1. Will Usher, Tom Russell, Roald Schoenmakers, Craig Robson, Fergus
   Cooper and Thibault Lestang | **nismod/smif v1.2.0** | *Zenodo* |
   2019 | ([doi](http://doi.org/10.5281/zenodo.1309336))

# <a name="community"></a> Community

## The Oxford Code Review Network

As a researcher it's often difficult to feedback on your codes.  Is
your code readable and understandable by someone else? Are you missing
out on some good programming practice(s)? Would somebody else have taken
a different approach to solve the problem at hand?

These questions can be answered through engaging in regular code
reviews, i.e. sitting down with a few colleagues and discussing a
chunk of your code. It's a time for friendly conversation, debate and
knowledge transfer that results and an improved code, strengthened
team-spirit and better/wider software skills. Code reviews are fairly
common in industry, but quasi non-existent in academia. In July 2020 I
initiated the [Oxford Code Review Network](https://github.com/OxfordCodeReviewNet/forum),to promote code reviewing in
academia and facilitate code reviews between researchers across the
University Of Oxford, by providing a (online) forum - for now a GitHub
repo - for researchers across Oxford to get in touch and do code
reviews together.

I'm convinced than making code reviewing a standard practice in
academic research can have a tremendous impact on the quality of
research software as a whole, not only resulting from the reviews
themselves, but also by enabling the sharing of software skills and
knowledge across levels of experience, backgrounds and research
communities.  I feel like this is much needed.

## Reproducible research Oxford

I've been a [Reproducible Research Oxford](https://ox.ukrn.org/)
(RROx) fellow since May 2020. RROx is the local Oxford branch of the
wider [UK Reproducibility Network](https://www.ukrn.org/), and
organisation of academics that works towards the culture change
required to make open and reproducible research the norm.

RROx is a very active group, hosting/supporting various seminars,
training events and grassroots initiatives such as
[reproducibiliTea](https://reproducibilitea.org/journal-clubs/#Oxford)
Oxford, the [Oxford Code Review
Network](https://github.com/OxfordCodeReviewNet/forum) and the Oxford
Free and Open Source Software group.


## Oxford Free/Open Source Software (OxFOSS)

Together with Laura Fortunato, Rowan Wilson and Malika Ihle, we
initiated a local interest group on free (as in free speech)
software. The motivation was simple: as supporters of free
software, there was no local group to get involved with and meet other
free software supporters/activists. So we decided to start our own.

OxFOSS officially started in October 2020 as a very informal biweekly
meeting open to anybody who wants to talk free software. Meeting are a
combination of relaxed chats on a predefined topic and invited
talks. We hope that these will foster a strong and friendly free
software community in Oxford, that can give free software more visibility
for academics but also outside the University.

If you're interested, you can [subscribe to the OxFOSS mailing
list](https://web.maillist.ox.ac.uk/ox/subscribe/foss) and/or [join
our Matrix
room](https://chat.cs.ox.ac.uk/#/room/#oxfoss-general:cs.ox.ac.uk). If
you're not working at the University Of Oxford, feel free [to get in
touch](mailto:thibault.lestang@cs.ox.ac.uk) with me and I can add you
to the room.

## Junior Research Fellowship at Kellogg College

In may 2020 I was awarded a Junior Research Fellowship from [Kellogg
College](https://www.kellogg.ox.ac.uk/), starting
October 2020. Despite the pandemic, I'm very excited to take part in
the College's life and connect with students and other fellows.  I see
this fellowship as a great opportunity to make research software
engineering more visible but also learn more about where and how is
research software developed across research fields and communities. I
believe than research software engineers can bring a lot to colleges,
and I am very grateful to Kellogg College for giving me the
opportunity to demonstrate this!

# <a name="courses"></a> Courses

A crucial part of our mission at [Oxford Research Software
Engineering](https://www.rse.ox.ac.uk/) is to deliver training courses
to the local research community. You can find the list of courses that
we run regularly [here](https://www.rse.ox.ac.uk/training/).  Feel
free to get in touch if you'd like us to run a course for your
team/lab/department.  Among them, I'm responsible for the following:

## Python packaging

A three hours course on organising and sharing python projects, using
python packages.

Participants start with a couple of messy analysis scripts that they
incrementally turn into a full blown python package they finally
release on PyPI (well, TestPyPI to be accurate).

This course gives researchers who write python to tools to organise
their projects in a way that makes reusing code straightforward, but
also efficient and sustainable.  It also demonstrates that sharing
this code with others - beyond exchanging USB sticks - is very
simple. Anyone can make their python project "pip installable".
