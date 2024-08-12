# Material UDIM and Texel Density Management Add-on

## Overview

This Blender add-on provides tools for managing material UDIMs and adjusting texel density on mesh objects. The add-on introduces a custom panel in the UV/Image Editor, offering operators to count materials, generate UDIM tiles based on materials, and adjust/apply texel density using an external Texel Density Checker add-on.

## Features

### 1. Material UDIM Panel
- **Location:** UV/Image Editor > Sidebar > Material UDIM
- **Controls:**
  - **Count Materials:** Counts the number of materials assigned to the active mesh object.
  - **Generate UDIM:** Moves UVs to different UDIM tiles based on the materials assigned to the active mesh object.
  - **Texel Density Value:** Input field to set the desired texel density.
  - **Apply Texel Density:** Applies the specified texel density to each material on the active mesh object.

### 2. Operators
- **CountMaterialsOperator**
  - **ID:** `uv.count_materials`
  - **Description:** Counts the number of materials on the active mesh object and updates the material count displayed in the panel.

- **GenerateUDIMOperator**
  - **ID:** `uv.generate_udim`
  - **Description:** Automatically distributes UVs across different UDIM tiles based on the material index.

- **AdjustTexelDensityOperator**
  - **ID:** `uv.adjust_texel_density`
  - **Description:** Adjusts the texel density for the active object using the Texel Density Checker add-on.

- **ApplyTexelDensityOperator**
  - **ID:** `uv.apply_texel_density`
  - **Description:** Applies the specified texel density to each material on the active mesh object, reporting the status of each operation to Blender's Info window.

## Installation

1. Download or clone the repository.
2. Open Blender and go to `Edit > Preferences > Add-ons`.
3. Click `Install...` and select the `material_udim_addon.zip` file or the folder containing these scripts.
4. Enable the add-on by checking the box next to "Material UDIM".

## Usage

1. Select a mesh object in Object Mode.
2. Open the UV/Image Editor and go to the Material UDIM panel in the Sidebar.
3. Use the buttons in the panel to count materials, generate UDIMs, adjust texel density, and apply the texel density to your object.

## Requirements

- **Blender:** Version 4.2.0 or higher.
- **Texel Density Checker Add-on:** Ensure that this add-on is installed and enabled for the texel density operators to work properly.

## Author

**Rodrigo Camacho**

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your changes.
