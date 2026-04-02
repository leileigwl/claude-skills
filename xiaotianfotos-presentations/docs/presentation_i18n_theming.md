# Presentation Localization and Theming Design

## Objectives
- Enable runtime switching between supported locales for all textual content within a deck.
- Provide light and dark presentation styles, and allow future expansion to additional visual themes.
- Centralize background, theme, and locale control so a slide deck presents a consistent experience that follows Tailwind CSS utility conventions.

## Guiding Principles
- **Single source of truth**: Locale, theme, and background live in a shared presentation context to keep the UI consistent.
- **Separation of concerns**: Background visuals, typography tokens, and textual content are decoupled but coordinated through clearly defined interfaces.
- **Tailwind-first**: Themes are expressed through CSS variables and Tailwind utility classes to minimize custom CSS and keep design tokens declarative.
- **Accessible defaults**: Respect user OS preferences, provide high-contrast palettes, and guarantee minimum color contrast.
- **Persist intent**: If a deck opts into persistence, remember the user's locale and theme along with background selection.

## Requirements
### Localization
- All deck copy must be supplied via locale dictionaries. Each slide has an `id` that keys into the dictionaries.
- Provide deck-level metadata (title, presenter, etc.) and slide-level content (headings, body, bullets) in every supported locale.
- Support runtime switching without page reloads and emit an event so dependent components (e.g., charts) react.
- Use a fallback locale when a translation is missing (`en` by default) and surface missing keys during development.
- Allow per-slide overrides (e.g., technical terms) through a scoped translation helper.

### Theming (Light/Dark + Future Styles)
- Define a `ThemeDefinition` with semantic tokens: `surface`, `surfaceMuted`, `textPrimary`, `textMuted`, `accent`, `border`, etc.
- Expose Tailwind-compatible CSS custom properties on the `:root` (global) and `body[data-theme="…"]` scopes.
- Ship two first-class themes: `light` and `dark`. Additional styles (e.g., `minimal`, `vivid`) inherit from these tokens.
- Guarantee compatibility with background layers: backgrounds must adapt typography/border tokens for contrast.
- Respect the `prefers-color-scheme` media query for initial selection when persistence is disabled.

### Background Coordination
- Background selection must be aware of the active theme; backgrounds may provide theme-aware variants.
- When backgrounds declare `supportsTheme: true`, the manager picks the appropriate variant (`light`/`dark`).
- Background styles fall back to a neutral variant if the theme-specific asset is absent.

### Persistence and Context Boundaries
- Context keys (`contextKey`) scope persistence per deck or presentation.
- LocalStorage keys follow `ppt-preferences:{contextKey}` storing `{ backgroundId, themeId, locale }`.
- Optional session-only behaviour toggled via props.

## Proposed Architecture
### Shared Presentation Context
- Create a composable `usePresentationContext` that exposes reactive state and actions:
  ```ts
  interface PresentationPreferences {
    backgroundId: string
    themeId: ThemeId
    locale: LocaleCode
  }

  interface PresentationContext {
    state: DeepReadonly<PresentationPreferences>
    backgrounds: BackgroundDefinition[]
    themes: ThemeDefinition[]
    locales: LocaleMeta[]
    setLocale(locale: LocaleCode): void
    setTheme(themeId: ThemeId): void
    setBackground(backgroundId: string): void
    resetToDefaults(): void
  }
  ```
- Implement as a lightweight store (Pinia or provide/inject pattern) initialized by the deck shell component.
- Background manager subscribes to this context instead of holding local-only state.

### Localization Module
- Store dictionaries under `src/locales/{locale}/deck-{deckId}.json`.
- Provide a helper `createDeckI18n(deckId, supportedLocales)` that loads dictionaries (statically via Vite + dynamic imports).
- Expose a formatter (`t(key, params?)`) that reads from the context's locale and falls back to default.
- During development, log missing keys and highlight them visually (e.g., wrap with `??key??`).

### Theming Module
- Define `src/shared/theme/themes.ts` exporting `ThemeDefinition[]` with token maps.
- Populate Tailwind config (`tailwind.config.js`) to read from CSS variables, e.g.:
  ```js
  extend: {
    colors: {
      surface: 'rgb(var(--surface) / <alpha-value>)',
      text: 'rgb(var(--text-primary) / <alpha-value>)',
      accent: 'rgb(var(--accent) / <alpha-value>)',
    },
  }
  ```
- Provide a Vue directive or composable `useApplyTheme(themeId)` that updates `document.documentElement` data attributes and variables.
- Pair each theme with typography scale guidelines (e.g., `text-3xl` for titles, `tracking-tight` for headings) documented per slide type.

### Background Manager Extension
- Convert `background-manager.vue` to consume the shared context: listen to `state.themeId` and `state.locale`.
- Update props/events to coordinate with the new context (e.g., emit `change:theme` and `change:locale`).
- When theme changes, propagate to Tailwind via `useApplyTheme` and update background variant.

## Slide Authoring Guidelines
- **Structural tokens**: Titles use `text-4xl font-semibold`, body copy `text-base leading-relaxed`, captions `text-sm text-text-muted`.
- **Spacing**: Utilize Tailwind spacing units (`py-12`, `px-16`) to keep layout consistent across themes.
- **Locale considerations**:
  - Keep translation keys descriptive (`slide01.title`, `agenda.list.0`).
  - Provide short/long variants if text expansion differs significantly across locales.
  - Support RTL locales by toggling `dir` attribute when `locale.meta.direction === 'rtl'`.
- **Theme considerations**:
  - Avoid hard-coded colors; rely on tokens (`bg-surface`, `text-text`, `border-border`).
  - Use `mix-blend-mode` sparingly; ensure contrast in both light/dark backgrounds.

## Interaction Flows
1. **Initialization**: Deck shell reads defaults (`defaultLocale`, `defaultTheme`, `defaultBackground`). If persistence is enabled, merge stored preferences.
2. **User toggles theme**: Call `setTheme`. Context updates state, `useApplyTheme` writes CSS vars, background manager re-renders with theme variant.
3. **User toggles locale**: Call `setLocale`. Translation composable updates reactive computed strings, slides re-render with new text.
4. **Background change**: `setBackground` selects variant based on active theme and emits metrics if needed.

## Persistence Strategy
- Serialize preferences on change with a small debounce (e.g., 150 ms) to avoid rapid writes.
- Clear stored preferences if the deck revokes persistence (guarded by versioning key `ppt-preferences:v1`).

## Testing Strategy
- Unit test the context store to ensure theme/locale/background updates propagate correctly.
- Snapshot test slide rendering per locale/theme combination for key decks.
- Integration test keyboard shortcuts (e.g., `Ctrl/Cmd + Shift + P`) for opening settings, plus new shortcuts for theme/locale toggles if added.

## Implementation Roadmap
1. Scaffold shared context, theme definitions, and localization loader.
2. Integrate Tailwind tokens and update existing slide components to consume CSS variables.
3. Extend `background-manager.vue` to delegate to context and support theme-aware backgrounds.
4. Build UI controls for language and theme selection within the settings overlay.
5. Add persistence, fallback handling, and automated tests.
