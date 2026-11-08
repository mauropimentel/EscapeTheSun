# Beta 2.0 — fast MVP release checklist

## Included in the MVP

- [x] 20 Old Dubai levels and sequential progression.
- [x] Main menu, local player name, local scoreboard, closet.
- [x] Sun Coins, guarded purchases, replay rewards.
- [x] Level completion summary with stars, score and coin reward.
- [x] Original Android icon and launch artwork.
- [x] Offline fallback illustrations for landmarks.
- [x] Debug APK workflow and unsigned release AAB validation.

## Before inviting external testers

- [ ] Validate all 20 levels on physical Android devices, including restart, next level, level locks, coins and purchases.
- [ ] Verify persistence after app upgrades; do not clear application data between tests.
- [ ] Confirm splash behavior on Android 12+ and cold starts.
- [ ] Test airplane mode, small screens, foldable devices and accessibility/reduced-motion settings.
- [ ] Check local storage data migration from previous betas.
- [ ] Confirm licensed landmark images and attribution, or ship with offline illustrations only and remove third-party image loading.
- [ ] Add a published privacy policy with verified contact information.
- [ ] Freeze Android application ID and establish a monotonic versionCode.
- [ ] Generate and securely back up upload keystore; configure signed AAB build without committing credentials.
- [ ] Complete Play Console declarations, screenshots, feature graphic and content rating.
- [ ] Run a closed testing track and address crash reports.

## Out of MVP scope

Online accounts, global username uniqueness, cloud saves, anti-cheat online leaderboards, real ads, real-money purchases, Marina/Palm/Downtown levels.

## Release strategy

Keep the debug APK as an internal QA build. Publish a signed AAB only after completing the above checklist. Do not upload the unsigned CI artifact to Google Play.
