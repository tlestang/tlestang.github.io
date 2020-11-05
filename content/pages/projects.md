Title: Projects
Date: 2020-10-04 13:40
Summary: A list of past and current projects

# Current projects

## PyBaMM

Design and manufacturing of more efficient and resilient energy
storage solutions is a key effort towards the developmentt of
sustainable enery systems. Beyond our laptops and phones, batteries
allow the storage of energy from fluctuating renewabele energy sources
such as windfarm.  Increasingly, electricity-powered vehicales are
becoming reality, from cars all the way to small planes!

PyBaMM is a python package for designing, simulating and analysing
battery models. Development started in 2019 at the Mathematical
Institute (Univeristy of Oxford) and the project was soon adopted as
the common modeling framework for the Faraday Institution, the main
entity supporting battery research in the UK. Battery models are
traditionally solved using multi-scale modeling software such as
COMSOL. In contrast, PyBaMM is a free (as in freedom) package
available to all for use but also to contribute to. Beyond efficiently
solving battery models, PyBaMM aims at becoming a community tool,
developped by and for battery scientits.

## stochare

Stochastic models (understand mathematical models of random processes)
arise in many scientific fields: physics, chemistry, biology,
finance... Stochrare aims at providing a toolbox to support research
dealing with stochastic processes regardless of the application
domain. For instance:

- numerical integration of SDEs
- numerical solver for the Fokker-Planck equations
- first-passage time computation
- instanton computation
- rare event algorithms


Although the package was initially developed with an
out-of-equilibrium statistical physics point of view, it aims at
providing tools to support research with stochastic processes in any
of these fields.

# Past projects

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
modbile app. And app can be used by clinicians in Acute Stroke Units
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

We also implememted an automatic scoring system, with a results
overview being automatically generated at the end of each assessment
for the benefit of the clinician performing the screening. More
complete data is securely stored in a cloud database, and can be
downloaded for additional processing by Dr Vancleef and her team.

## Smif

Infrastructure systems (think water and energy supply, transport
systems...) provide essential basic services to society but can also
have harmful social and environmental impacts. Plans and decisions are
subject to uncertain socio-economic, technological and environmental
change and these complexities are best studied through simulation.
Smif[1,2] is a software framework for the integration of simulation
models of infrastructure systems such as energy, transport, water and
digital communications.

Smif enables the coupling and orchestration of an heterogeneous
ensemble of models: each model has its own space and time resolution,
set of inputs and outputs and data formats. To run under smif, models
must be wrapped by a well-defined Python class, which provides a
common interface. Smif’s purpose is to provide infrastructure systems
modellers a tool capable of handling the execution of the models
according to their dependencies, as well as the necessary data
exchange between models, transforming data if necessary.

The development of smif is driven by the National Infrastructure
Systems Model (NISMOD2), which consists of a collection of
high-resolution infrastructure models of the United Kingdom. However,
smif is a very general framework that can applied whenever models can
be executed from Python, via import, binding, or call out to a
command-line executable.

1. Will Usher and Tom Russell | **A Software Framework for the Integration of Infrastructure Simulation Models** | [*Journal of Open Research Software*](https://openresearchsoftware.metajnl.com/) | 2019 | ([doi](https://doi.org/10.5334/jors.265))

1. Will Usher, Tom Russell, Roald Schoenmakers, Craig Robson, Fergus Cooper and Thibault Lestang | **nismod/smif v1.2.0** | *Zenodo* | 2019 | ([doi](http://doi.org/10.5281/zenodo.1309336))
