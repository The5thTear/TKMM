<div align="center">
  <img src="https://github.com/The5thTear/TCML/assets/144561947/52758c78-0ab5-45ff-89ab-ccdab7b72567" width="300vh">
  <h1 style="font-family: Fira Sans">- &nbsp; Tears of the Kingdom Cross-Platform Mod Loader &nbsp; -</h1>
</div>

<p align="center" style="text-align: center;">
  <a href="https://github.com/The5thTear/TCML/releases">
    <img src="https://img.shields.io/github/v/tag/ArchLeaders/MalsMerger?style=for-the-badge&logoColor=C71B42&color=C71B42&labelColor=2A2C33&logo=github&label=Version" alt="Releases' YouTube"/>
  </a> &nbsp;
  <a href="https://discord.com/invite/w7qGa5RyMc">
    <img src="https://img.shields.io/discord/1179611100183011429?style=for-the-badge&logoColor=37C75E&color=37C75E&labelColor=2A2C33&logo=discord&label=discord" alt="Discord"/>
  </a> &nbsp;
  <a href="https://github.com/The5thTear/TCML">
    <img src="https://img.shields.io/github/stars/The5thTear/TCML?style=for-the-badge&logoColor=FFCB41&color=FFCB41&labelColor=2A2C33&logo=github" alt="Stars"/>
  </a>
</p>

**TCML**, an acronym for **T**ears of the Kingdom **C**ross-platform **M**od **L**oader (merger), is a versatile tool crafted to streamline modding across multiple platforms for the game *Tears Of The Kingdom*. **TCML** utilizes [dt-12345](https://github.com/dt-12345)'s RESTBL tool and seamlessly integrates with various mod merging tools, delivering a quick and satisfying experience for modders.

<p>
  <a href="https://github.com/The5thTear/TCML/issues">
    <img src="https://img.shields.io/github/issues/The5thTear/TCML?logoColor=red&color=red&logo=github&style=flat&labelColor=2A2C33" alt="Issues"/>
  </a> &nbsp;
  <a href="https://github.com/The5thTear/TCML/pulls">
    <img src="https://img.shields.io/github/issues-pr/The5thTear/TCML?style=flat&labelColor=2A2C33&logoColor=blue&color=blue&logo=github" alt="Open Pull Requests"/>
  </a> &nbsp;
  <a href="https://github.com/The5thTear/TCML/pulls">
    <img src="https://img.shields.io/github/issues-pr-closed/The5thTear/TCML?style=flat&labelColor=2A2C33&logoColor=5751FF&color=5751FF&logo=github" alt="Closed Pull Requests"/>
  </a>
</p>

## Mod Merging

TCML integrates with multiple mod merging tools to support the seamless combination of various file types.

### Current Supported File Types

* **ResourceSizeTable** support leverages [dt-12345](https://github.com/dt-12345)'s restbl tool for an efficient Resource Size Table (RSTB) estimation, and creation.
* **RSDB** *(Tag.Product, PouchActorInfo, GameActorInfo, etc.)* makes use of [Legend5v](https://gamebanana.com/members/2731522)'s original code with added QoL features for efficient and funtional merging.
* **Localization (Mals)** created by [Arch Leaders](https://github.com/ArchLeaders), his [MalsMerger](https://github.com/ArchLeaders/MalsMerger) is lightning fast, ensuring you recieve your merged files as fast as possible.
    
### Planned Support:
    
* **SARC:** Archives
* **BYML:** Parameter Files
* **BFRES:** Models
* **TXTG:** Textures

> Note: Priority-based merging for specific file types (e.g., SARC archives, bgyml, byml, bfres, txtg).

## Usage

### For Creators:

If you are a mod creator, and would like your mod to be fully supported by TCML, here are the steps you can follow:

> *(TCML will work without this, just some easy stuff to help visually assist end users)*

- Add a `meta.json` file with a structure like this:
  ```jsonc
  {
    "modName": "Your Mod Name",
    "description": "Description of your mod",
    "author": "Your Name",
    // Add any other relevant information
  }
  ```

- Add a thumbnail.png file with the thumbnail for your mod!

**TCML will now seamlessly merge your mod!**

---

### For Merging

This is how you prep your mod for perfect compatibility with TCML!

```
Add steps or instructions for mod merging compatibility here.
```

---

# Contributions and Special Thanks

```
(Insert Final Special Thanks Here)
```

<!--
TODO: Add MIT license?
e.g. https://github.com/ArchLeaders/MalsMerger/blob/master/License.md
-->

<!--[![License](https://img.shields.io/badge/License-MIT-blue.svg)](License.md)-->

*Join our Discord community [here](https://discord.com/invite/w7qGa5RyMc) if you'd like to contribute to the development of **TCML**. Your insights and collaboration are highly valued!*