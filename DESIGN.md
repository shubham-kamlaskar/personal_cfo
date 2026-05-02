---
colors:
  ink:
    value: "#05080f"
    description: "Primary dark background color"
  ink-2:
    value: "#1a2236"
    description: "Secondary dark surface"
  ink-3:
    value: "#3d4d6a"
    description: "Tertiary dark surface"
  muted:
    value: "#7a8aa8"
    description: "Muted text color"
  line:
    value: "rgba(255,255,255,0.08)"
    description: "Subtle border color"
  surface:
    value: "#0b1120"
    description: "Main surface background"
  card:
    value: "#0f1929"
    description: "Card background"
  card-2:
    value: "#131f32"
    description: "Secondary card background"
  blue:
    value: "#2563eb"
    description: "Primary blue"
  blue-2:
    value: "#3b82f6"
    description: "Light blue accent"
  cyan:
    value: "#06b6d4"
    description: "Cyan accent"
  emerald:
    value: "#10b981"
    description: "Success green"
  amber:
    value: "#f59e0b"
    description: "Warning amber"
  rose:
    value: "#f43f5e"
    description: "Error rose"
  white:
    value: "#ffffff"
    description: "Pure white"
  off:
    value: "#e8edf5"
    description: "Off-white text"

typography:
  display:
    family: "Bricolage Grotesque"
    weight: 800
    line-height: 1.05
    letter-spacing: -0.03em
    description: "Large display headings"
  heading:
    family: "Bricolage Grotesque"
    weight: 700
    letter-spacing: -0.02em
    description: "Section headings"
  body:
    family: "DM Sans"
    weight: 400
    line-height: 1.6
    description: "Body text"
  accent:
    family: "DM Sans"
    weight: 500
    description: "Emphasized body text"

spacing:
  xs: "0.25rem"
  sm: "0.5rem"
  md: "1rem"
  lg: "1.5rem"
  xl: "2rem"
  xxl: "3rem"
  xxxl: "4rem"

radii:
  sm: "8px"
  md: "10px"
  lg: "20px"
  xl: "99px"

shadows:
  sm: "0 2px 12px rgba(0,0,0,0.06)"
  md: "0 8px 30px rgba(37,99,235,0.35)"
  lg: "0 40px 80px rgba(0,0,0,0.6)"
  xl: "0 0 120px rgba(37,99,235,0.08)"

motion:
  duration:
    fast: "0.15s"
    normal: "0.2s"
    slow: "0.6s"
  easing:
    default: "ease"
    in: "ease-in"
    out: "ease-out"
    both: "ease-in-out"

elevation:
  level-1:
    shadow: "0 0 0 1px rgba(255,255,255,0.04)"
    description: "Subtle card elevation"
  level-2:
    shadow: "0 8px 30px rgba(37,99,235,0.35)"
    description: "Button hover elevation"
  level-3:
    shadow: "0 40px 80px rgba(0,0,0,0.6), 0 0 120px rgba(37,99,235,0.08)"
    description: "Hero card elevation"
---

# TaxCopilot Design System

TaxCopilot is an AI-powered tax benefit platform for Indian businesses, featuring a sophisticated dark-themed design that balances professional trust with modern aesthetics. The design system emphasizes clarity, efficiency, and user confidence through carefully crafted visual elements.

## Visual Identity

### Color Palette
The color system is built around a dark foundation with strategic accent colors. The primary ink color (#05080f) creates a sophisticated, trustworthy base that positions TaxCopilot as a professional financial tool. Blue serves as the primary action color, conveying reliability and technology, while cyan provides complementary accents. Semantic colors (emerald, amber, rose) ensure clear communication of status and feedback.

### Typography
Typography combines the geometric boldness of Bricolage Grotesque for headings with the clean readability of DM Sans for body text. This pairing creates hierarchy while maintaining approachability. The display style uses tight letter spacing and minimal line height for maximum impact in hero sections.

### Layout & Spacing
Spacing follows a consistent scale based on rem units, ensuring scalability across devices. The layout emphasizes generous whitespace and clear visual hierarchy, reducing cognitive load for users navigating complex tax information.

### Elevation & Depth
Shadows are used sparingly but purposefully. Subtle inner shadows on cards create depth without distraction, while hover states provide clear interactive feedback. The noise grain overlay adds texture that prevents the flatness common in dark designs.

## Design Principles

### Trust Through Sophistication
The dark theme with subtle gradients and noise texture creates a premium, trustworthy appearance appropriate for financial software. Every visual element reinforces reliability and professionalism.

### Clarity in Complexity
Tax information is inherently complex. The design system uses clear typography hierarchy, consistent spacing, and semantic color coding to make complex information digestible.

### Efficiency in Interaction
Interactive elements feature smooth transitions and clear hover states. The design minimizes clicks while maximizing information density through well-structured layouts.

### Accessibility Considerations
High contrast ratios ensure readability. The color palette maintains sufficient differentiation for color-blind users, and typography scales appropriately for various screen sizes.

## Component Variations

### Marketing Pages (Landing)
Features full design system implementation with gradients, animations, and sophisticated layouts optimized for conversion.

### Authentication Flows
Simplified light-theme variant using Bootstrap foundation with custom styling for consistency.

### Dashboard Interfaces
Light-theme data-focused layouts prioritizing functionality over visual flair, maintaining brand colors for cohesion.

### Admin Interfaces
Functional designs emphasizing data management with consistent spacing and typography from the core system.

## Implementation Notes

- All colors are defined as CSS custom properties for easy theming
- Typography uses Google Fonts for reliable cross-platform rendering
- Spacing scale ensures consistent proportions across all interfaces
- Motion design uses CSS transitions for smooth, performant animations
- Responsive design ensures usability across desktop, tablet, and mobile devices