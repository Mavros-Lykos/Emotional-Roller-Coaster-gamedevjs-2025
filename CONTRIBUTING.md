# Contributing to Emotional Roller Coaster

Thank you for your interest in contributing to Emotional Roller Coaster! This document provides guidelines and requirements for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Development Requirements](#development-requirements)
- [How to Contribute](#how-to-contribute)
- [Coding Standards](#coding-standards)
- [Pull Request Process](#pull-request-process)
- [GameDevJS Challenge Requirements](#gamedevjs-challenge-requirements)

## Code of Conduct

- Be respectful and inclusive in your communications
- Accept constructive criticism gracefully
- Focus on what is best for the community and the project
- Show empathy towards other community members

## Development Requirements

### Required Software

- [Ren'Py SDK](https://www.renpy.org/latest.html) (version 7.4.0 or higher)
- Text editor or IDE (Visual Studio Code recommended with Ren'Py Language extension)
- [Git](https://git-scm.com/downloads)
- Image editing software for assets (GIMP, Photoshop, etc.)

### Knowledge Requirements

- Basic understanding of Ren'Py scripting
- Understanding of Python (for advanced features)
- Familiarity with Git version control
- (If you have passion to learn and contribute, love to help you guys! and  highly encouraged !)

## How to Contribute

#### Help us as much as you can ! (even from commenting the code !)

### Reporting Bugs

1. Check if the bug has already been reported in the Issues section
2. Create a new issue with a clear title and description
3. Include steps to reproduce the bug
4. Add screenshots if applicable
5. Describe expected behavior vs actual behavior

### Suggesting Features

1. Check if the feature has been suggested in the Issues section
2. Create a new issue with [Feature] prefix in the title
3. Describe the feature and its benefits clearly
4. Consider including mockups or examples

### Code Contributions

1. Fork the repository
2. Create a new branch based on `main` with a descriptive name
3. Make your changes following our [coding standards](#coding-standards)
4. Test your changes thoroughly
5. Submit a pull request

## Coding Standards

### Ren'Py Scripting

- Use 4-space indentation
- Comment your code, especially complex logic
- Use labels for each scene/significant event
- Structure dialogue with character names clearly defined
- Keep lines of dialogue reasonably short (less than 80 characters)

Example:
```renpy
# Modify top screen text definitions:
screen top_text(t):
    frame:
        xalign 0.5
        yalign 0.05
        padding (20, 20)
        background "#0008"  # semi-transparent background
        has vbox:
            xalign 0.5
        add TypewriterText(Text(t, style="top_text_style"))

```

### Asset Organization

- Name files clearly and descriptively
- Use consistent naming conventions:
  - Backgrounds: `bg_location.png`
  - Characters: `char_name_expression.png`
  - GUI elements: `gui_element_state.png`
  - Music: `music_situation.ogg`
  - Sound effects: `sfx_action.ogg`

## Pull Request Process

1. Update the README.md/documentation with details of changes if applicable
2. Make sure your code follows our standards and passes all tests
3. Fill out the pull request template completely
4. Request review from a maintainer
5. Maintainers will merge the PR once approved

## GameDevJS Challenge Requirements

As this project is participating in the GameDevJS GitHub Challenge, all contributions should help maintain compliance with the challenge requirements:

1. **Well-documented code**: All code should be properly commented and follow the project's documentation standards
   
2. **Clear README**: Any changes to functionality should be reflected in the README.md

3. **Public repository structure**:
   - Keep the repository organized according to the established structure
   - Ensure assets are properly credited
   - Maintain separation between code, assets, and documentation

4. **Past winner qualities to emulate**:
   - Innovative gameplay mechanics
   - High-quality documentation
   - Clean, maintainable code
   - Creative narrative elements
   - Polished user experience

5. **Tag commits appropriately**:
   - Use prefixes like `[Feature]`, `[Fix]`, `[Docs]`, etc.
   - Write clear, concise commit messages

For more information on the GameDevJS GitHub Challenge, visit the [official website](https://gamedevjs.com/challenge/).

---

Thank you for contributing to Emotional Roller Coaster!