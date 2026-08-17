<p align="center">
  <img src="docs/images/banner.png" alt="IberOSINT Banner">
</p>

<h1 align="center">IberOSINT</h1>

<p align="center">
<b>Unified Open Source Intelligence Platform</b><br>
A modular ecosystem for Open Source Intelligence, cybersecurity investigations and AI-assisted analysis.
</p>

<p align="center">

<a href="README.md">🇪🇸 Español</a> | <b>🇬🇧 English</b>

</p>

<p align="center">

![Platform](https://img.shields.io/badge/Platform-Ubuntu-E95420?style=for-the-badge)

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)

![OSINT](https://img.shields.io/badge/OSINT-Research-blue?style=for-the-badge)

![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Investigation-red?style=for-the-badge)

![AI](https://img.shields.io/badge/Artificial_Intelligence-Integrated-success?style=for-the-badge)

![Status](https://img.shields.io/badge/Status-Active_Development-success?style=for-the-badge)

</p>

---

# What is IberOSINT?

**IberOSINT** is a modular platform designed to centralize Open Source Intelligence (OSINT) tools, automate investigative workflows and enhance information analysis through Artificial Intelligence within a unified working environment.

The platform brings together several specialized applications under a single graphical interface, allowing analysts to access OSINT resources, investigation tools, automation features and AI-powered assistants without relying on multiple independent platforms.

Rather than being a simple collection of tools, IberOSINT provides a structured, scalable ecosystem focused on improving the efficiency of cybersecurity investigations, threat intelligence and digital research.

---

# Project Background

IberOSINT was originally developed as a **Master's Thesis** within the **Master's Degree in Cybersecurity** at the **Universidad Católica de Murcia (UCAM), Spain**.

The initial objective was to build a Linux-based distribution focused on Open Source Intelligence by integrating multiple investigation tools into a single working environment.

As development progressed, the project evolved far beyond its original academic scope into a modular ecosystem composed of custom applications specifically designed to support digital investigations, automation and AI-assisted analysis.

Today, IberOSINT continues to evolve as an independent research and development project.

---

# Design Philosophy

The development of IberOSINT is based on five fundamental principles:

- Centralize access to OSINT resources.
- Reduce time spent on repetitive investigative tasks.
- Assist analysts through workflow automation.
- Use Artificial Intelligence as analytical support, never as a replacement for human judgment.
- Maintain a modular architecture that can easily evolve over time.

---

# Why IberOSINT?

Unlike many similar projects, IberOSINT is not intended to be just another collection of cybersecurity tools.

Its goal is to provide a unified workspace where every module plays a specific role within the intelligence gathering and investigation process.

Key features include:

- Modular Python-based architecture.
- Dedicated graphical interface.
- Integrated OSINT workspace.
- Specialized Firefox and Tor Browser environments.
- Artificial Intelligence integration.
- Workflow automation.
- Centralized tool management.
- Scalable architecture.
- Consistent user experience across all modules.

---

# Overall Architecture

The IberOSINT ecosystem consists of several specialized applications working together under a single Launcher.

```

                    IberOSINT
                         │
        ┌────────────────┼────────────────┐
        │                │                │
 IberoFirefox      IberoTOR       IberoTOOLS
        │                │                │
        └────────────────┼────────────────┘
                         │
                  IberOSINT AI
                         │
                       Lince
                         │
                     Tutorials

```

Each module has been designed to address a specific stage of the OSINT investigation workflow while maintaining a modular architecture that simplifies future maintenance and expansion.

---

# The IberOSINT Ecosystem

IberOSINT is composed of several specialized applications designed to support every stage of an Open Source Intelligence investigation.

Each module addresses a specific operational need while sharing a common design philosophy, a consistent user experience and seamless integration through the main Launcher.

---

# Launcher

The Launcher serves as the central entry point to the entire IberOSINT ecosystem.

Through a single graphical interface, users can access every available module, organize their workspace and launch all integrated applications without leaving the platform.

Its primary objective is to simplify the investigative workflow by providing a unified and intuitive working environment.

### Main Features

- Python-based graphical interface.
- Centralized access to all ecosystem modules.
- Latest News Section from INCIBE and MuySeguridad.
- Modular and scalable architecture.
- Intuitive organization of tools.
- Integration with external applications.

<p align="center">
<img src="docs/images/launcher.png" alt="Launcher" width="95%">
</p>

*Main launcher interface.*

---

# IberoFirefox

IberoFirefox is a dedicated OSINT workspace built around Firefox, providing fast access to hundreds of carefully organized intelligence resources.

Instead of searching for investigation tools across multiple websites, analysts can access a centralized homepage where resources are grouped into logical categories for quick navigation.

The homepage has been developed entirely using HTML, CSS and JavaScript and operates locally without relying on external services.

### Main Features

- Custom OSINT homepage.
- Categorized intelligence resources.
- Integrated search engine.
- Favorites management.
- Recently used resources.
- Investigation-oriented interface.
- Fully offline operation.

<p align="center">
<img src="docs/images/iberofirefox.png" alt="IberoFirefox" width="95%">
</p>

*Integrated OSINT workspace for Firefox.*

---

# IberoTOR

IberoTOR extends the same philosophy to Tor Browser, providing an investigation environment specifically designed for situations where anonymous browsing is required.

It maintains the same organizational structure and user experience as IberoFirefox while focusing on resources and workflows that benefit from the privacy offered by the Tor network.

### Main Features

- Tor Browser integration.
- Anonymous OSINT workspace.
- Centralized access to investigation resources.
- Category-based organization.
- Consistent interface across the ecosystem.

<p align="center">
<img src="docs/images/iberotor.png" alt="IberoTOR" width="95%">
</p>

*OSINT workspace designed for Tor Browser.*

---

# IberoTOOLS

IberoTOOLS provides centralized management of the tools installed within the platform, allowing investigators to launch utilities directly from the graphical interface without remembering commands or installation paths.

Its modular design makes it easy to incorporate additional applications as the ecosystem continues to grow.

### Main Features

- Centralized tool management.
- Fast access to installed applications.
- Modular architecture.
- Organized by categories.
- Seamless Launcher integration.

<p align="center">
<img src="docs/images/iberotools.png" alt="IberoTOOLS" width="95%">
</p>

*Unified management of integrated investigation tools.*

---

# IberOSINT AI

IberOSINT AI introduces Artificial Intelligence capabilities into the platform to assist analysts throughout different stages of an investigation.

Rather than replacing human expertise, AI is used to support evidence interpretation, automate repetitive tasks, summarize information and improve analytical efficiency.

The architecture has been designed to support multiple AI providers while maintaining a consistent user experience.

### Main Features

- Multi-provider AI integration.
- AI-assisted investigations.
- Workflow automation.
- Modular architecture.
- Easily extensible design.

<p align="center">
<img src="docs/images/iberosint-ai.png" alt="IberOSINT AI" width="95%">
</p>

*Artificial Intelligence services integrated into the platform.*

---

# Lince

Lince is the document analysis component of the IberOSINT ecosystem.

It enables investigators to process digital evidence, perform AI-assisted document analysis, extract Indicators of Compromise (IOCs), generate structured reports and support decision-making during cybersecurity investigations.

Its development has focused on combining advanced automation with an intuitive user interface that always keeps the analyst in control.

### Main Features

- AI-assisted document analysis.
- Multi-evidence processing.
- Automatic IOC extraction.
- Structured report generation.
- IOC dashboard.
- Multiple AI provider support.

<p align="center">
<img src="docs/images/lince.png" alt="Lince" width="95%">
</p>

*Lince document analysis platform.*

---

# Tutorials

The Tutorials module provides practical documentation intended to help users make the most of the IberOSINT ecosystem.

It includes step-by-step guides, technical references and best practices covering both the platform itself and the integrated investigation tools.

The documentation is organized progressively, making it suitable for both new users and experienced cybersecurity professionals.

### Main Features

- Step-by-step guides.
- Technical documentation.
- Best practices.
- Learning resources.
- Continuously expanding knowledge base.

<p align="center">
<img src="docs/images/tutoriales.png" alt="Tutorials" width="95%">
</p>

*Integrated learning and documentation center.*

---

# Technologies

IberOSINT combines modern development technologies with a modular architecture to provide a unified platform for Open Source Intelligence, cybersecurity investigations and AI-assisted analysis.

| Technology | Purpose |
|------------|---------|
| Python | Launcher and core application development |
| CustomTkinter | Desktop graphical interface |
| HTML5 | OSINT homepage development |
| CSS3 | User interface styling |
| JavaScript | Dynamic homepage functionality |
| Bash | Automation and scripting |
| Ubuntu Linux | Base operating system |
| Firefox | Primary OSINT workspace |
| Tor Browser | Anonymous investigation environment |
| Ollama | Local AI model execution |
| Google Gemini | Cloud-based Artificial Intelligence |

---

# Requirements

The recommended environment for running IberOSINT is:

- Ubuntu 24.04 LTS or later.
- Python 3.11 or newer.
- Firefox.
- Tor Browser.
- Internet connection for accessing OSINT resources.
- Ollama (optional, for local AI models).
- Google Gemini API key (optional, for cloud AI features).

---

# Installation

Clone the repository:

```bash
git clone https://github.com/JSantos1990/IberOSINT.git
```

Navigate to the project directory:

```bash
cd IberOSINT
```

Launch the application:

```bash
python app.py
```

> **Note:** Some modules require third-party tools or external services to be installed and configured beforehand.

---

# Project Status

IberOSINT is under active development.

Thanks to its modular architecture, new tools, services and capabilities can be integrated without affecting the rest of the platform.

The project currently consists of multiple custom-developed applications working together to provide a unified environment for OSINT investigations and AI-assisted cybersecurity analysis.

---

## Future Development

- [ ] Tool Marketplace
- [ ] Plugin system
- [ ] Integrated updater
- [ ] Additional OSINT modules
- [ ] Support for new AI providers

---

# Screenshots

## Launcher

<img src="docs/images/launcher.png" alt="Launcher">

---

## IberoFirefox

<img src="docs/images/iberofirefox.png" alt="IberoFirefox">

---

## IberoTOR

<img src="docs/images/iberotor.png" alt="IberoTOR">

---

## IberoTOOLS

<img src="docs/images/iberotools.png" alt="IberoTOOLS">

---

## Lince

<img src="docs/images/lince.png" alt="Lince">

---

# License

Copyright © 2026 Jorge Santos

All Rights Reserved.

This project was originally developed as part of a Master's Thesis in Cybersecurity and has since evolved into an independent research and development initiative.

The source code, documentation, images and all other resources contained within this repository are the intellectual property of the author.

No part of this repository may be copied, modified, redistributed or used, in whole or in part, without the prior written permission of the author.

For further information, please refer to the **LICENSE** file included in this repository.

---

# Author

## Jorge Santos

Developer of IberOSINT.

Originally created as a Master's Thesis in Cybersecurity (UCAM), IberOSINT has grown into an independent platform focused on Open Source Intelligence, cybersecurity automation and AI-assisted investigations.

GitHub:

https://github.com/JSantos1990

---

# Acknowledgements

Special thanks to the Open Source community and to all developers whose projects, tools and documentation continue to advance the fields of cybersecurity and Open Source Intelligence.

---

<p align="center">

<strong>IberOSINT</strong><br>

Unified Open Source Intelligence Platform

<br><br>

© 2026 Jorge Santos · All Rights Reserved

</p>
