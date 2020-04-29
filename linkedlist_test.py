





<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://github.githubassets.com">
  <link rel="dns-prefetch" href="https://avatars0.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars1.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars2.githubusercontent.com">
  <link rel="dns-prefetch" href="https://avatars3.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">



  <link crossorigin="anonymous" media="all" integrity="sha512-FG+rXqMOivrAjdEQE7tO4BwM1poGmg70hJFTlNSxjX87grtrZ6UnPR8NkzwUHlQEGviu9XuRYeO8zH9YwvZhdg==" rel="stylesheet" href="https://github.githubassets.com/assets/frameworks-146fab5ea30e8afac08dd11013bb4ee0.css" />
  
    <link crossorigin="anonymous" media="all" integrity="sha512-YLhIrNR1DbhMpenrkxidvzDzbBGUd/nrcerKVRovUNkPAve1+7ndbBDQruPfut7uO2AxHoja5mSlqYAYtLhV4w==" rel="stylesheet" href="https://github.githubassets.com/assets/github-60b848acd4750db84ca5e9eb93189dbf.css" />
    
    
    
    


  <meta name="viewport" content="width=device-width">
  
  <title>CS-1.3-Core-Data-Structures/linkedlist_test.py at master · Make-School-Courses/CS-1.3-Core-Data-Structures</title>
    <meta name="description" content="CS 1.3: Core Data Structures &amp; Algorithms – Course Syllabus and Lessons - Make-School-Courses/CS-1.3-Core-Data-Structures">
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    <meta name="twitter:image:src" content="https://avatars0.githubusercontent.com/u/26469999?s=400&amp;v=4" /><meta name="twitter:site" content="@github" /><meta name="twitter:card" content="summary" /><meta name="twitter:title" content="Make-School-Courses/CS-1.3-Core-Data-Structures" /><meta name="twitter:description" content="CS 1.3: Core Data Structures &amp; Algorithms – Course Syllabus and Lessons - Make-School-Courses/CS-1.3-Core-Data-Structures" />
    <meta property="og:image" content="https://avatars0.githubusercontent.com/u/26469999?s=400&amp;v=4" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="Make-School-Courses/CS-1.3-Core-Data-Structures" /><meta property="og:url" content="https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures" /><meta property="og:description" content="CS 1.3: Core Data Structures &amp; Algorithms – Course Syllabus and Lessons - Make-School-Courses/CS-1.3-Core-Data-Structures" />

  <link rel="assets" href="https://github.githubassets.com/">
  <link rel="web-socket" href="wss://live.github.com/_sockets/VjI6NTA1NDY4NTEzOjdhNWU1ZjQ2M2M1ODczNTFlNzM4N2YyN2FlMzhjYmM2ZGI4ZDgyMGJlNjFhNjhmZmJjOWE4MGViOTYwOWU1MWQ=--b9f12627ac5fa2322d29a5e22adbda229763d8ef">
  <link rel="sudo-modal" href="/sessions/sudo_modal">

  <meta name="request-id" content="FAFB:9DEE:17C2B5:204687:5EA8CC1D" data-pjax-transient="true" /><meta name="html-safe-nonce" content="c78b79504878a9015c2d4825a2e278581174c2de" data-pjax-transient="true" /><meta name="visitor-payload" content="eyJyZWZlcnJlciI6Imh0dHBzOi8vZ2l0aHViLmNvbS9NYWtlLVNjaG9vbC1Db3Vyc2VzL0NTLTEuMy1Db3JlLURhdGEtU3RydWN0dXJlcy90cmVlL21hc3Rlci9Db2RlL2xpbmtlZC1saXN0IiwicmVxdWVzdF9pZCI6IkZBRkI6OURFRToxN0MyQjU6MjA0Njg3OjVFQThDQzFEIiwidmlzaXRvcl9pZCI6Ijg2Mzk2ODgzMjc5NjM1MzI1MDIiLCJyZWdpb25fZWRnZSI6InNlYSIsInJlZ2lvbl9yZW5kZXIiOiJpYWQifQ==" data-pjax-transient="true" /><meta name="visitor-hmac" content="df848e30a2b80244ebc5f6f0ae31c8bfe28c43b9e21b7bb007ec232f0b6abe6b" data-pjax-transient="true" />



  <meta name="github-keyboard-shortcuts" content="repository,source-code" data-pjax-transient="true" />

  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

    <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
  <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
  <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">

<meta name="octolytics-host" content="collector.githubapp.com" /><meta name="octolytics-app-id" content="github" /><meta name="octolytics-event-url" content="https://collector.githubapp.com/github-external/browser_event" /><meta name="octolytics-dimension-ga_id" content="" class="js-octo-ga-id" /><meta name="octolytics-actor-id" content="10855238" /><meta name="octolytics-actor-login" content="RobotGyal" /><meta name="octolytics-actor-hash" content="9ede87ce8cde50e521fadf87bbef16fab60af201513461afc51a71f636132540" />
<meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" />



    <meta name="google-analytics" content="UA-3769691-2">

  <meta class="js-ga-set" name="userId" content="726d88186946b679a29d4b5b151f617e">

<meta class="js-ga-set" name="dimension1" content="Logged In">



  

      <meta name="hostname" content="github.com">
    <meta name="user-login" content="RobotGyal">

      <meta name="expected-hostname" content="github.com">

      <meta name="js-proxy-site-detection-payload" content="YTQ2OWMwMTIzZDEwZGJkYmQ2Mjg2YmFjZjE3NjA3OGU3MDA0YThkYWNmNTYwZWJjYTJjZDE4NTYyMjE5NzE4Znx7InJlbW90ZV9hZGRyZXNzIjoiMTIuMjMyLjIxNS45MCIsInJlcXVlc3RfaWQiOiJGQUZCOjlERUU6MTdDMkI1OjIwNDY4Nzo1RUE4Q0MxRCIsInRpbWVzdGFtcCI6MTU4ODEyMDYwOCwiaG9zdCI6ImdpdGh1Yi5jb20ifQ==">

    <meta name="enabled-features" content="MARKETPLACE_SOCIAL_PROOF_CUSTOMERS,MARKETPLACE_TRENDING_SOCIAL_PROOF,MARKETPLACE_RECOMMENDATIONS,MARKETPLACE_PENDING_INSTALLATIONS,GHE_CLOUD_TRIAL,PAGE_STALE_CHECK">

  <meta http-equiv="x-pjax-version" content="595169291bf6d11dd3c17c5e1156eaca">
  

      <link href="https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/commits/master.atom" rel="alternate" title="Recent Commits to CS-1.3-Core-Data-Structures:master" type="application/atom+xml">

  <meta name="go-import" content="github.com/Make-School-Courses/CS-1.3-Core-Data-Structures git https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures.git">

  <meta name="octolytics-dimension-user_id" content="26469999" /><meta name="octolytics-dimension-user_login" content="Make-School-Courses" /><meta name="octolytics-dimension-repository_id" content="164776962" /><meta name="octolytics-dimension-repository_nwo" content="Make-School-Courses/CS-1.3-Core-Data-Structures" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="164776962" /><meta name="octolytics-dimension-repository_network_root_nwo" content="Make-School-Courses/CS-1.3-Core-Data-Structures" /><meta name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" content="false" />


    <link rel="canonical" href="https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://github.githubassets.com/pinned-octocat.svg" color="#000000">
  <link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon.png">
  <link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon.svg">

<meta name="theme-color" content="#1e2327">


  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="logged-in env-production page-responsive page-blob">
    

    <div class="position-relative js-header-wrapper ">
      <a href="#start-of-content" class="p-3 bg-blue text-white show-on-focus js-skip-to-content">Skip to content</a>
      <span class="Progress progress-pjax-loader position-fixed width-full js-pjax-loader-bar">
        <span class="progress-pjax-loader-bar top-0 left-0" style="width: 0%;"></span>
      </span>

      
      



          <header class="Header py-lg-0 js-details-container Details flex-wrap flex-lg-nowrap p-responsive" role="banner">
  <div class="Header-item d-none d-lg-flex">
    <a class="Header-link" href="https://github.com/" data-hotkey="g d"
  aria-label="Homepage " data-ga-click="Header, go to dashboard, icon:logo">
  <svg class="octicon octicon-mark-github v-align-middle" height="32" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>
</a>

  </div>

  <div class="Header-item d-lg-none">
    <button class="Header-link btn-link js-details-target" type="button" aria-label="Toggle navigation" aria-expanded="false">
      <svg height="24" class="octicon octicon-three-bars" viewBox="0 0 12 16" version="1.1" width="18" aria-hidden="true"><path fill-rule="evenodd" d="M11.41 9H.59C0 9 0 8.59 0 8c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zm0-4H.59C0 5 0 4.59 0 4c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zM.59 11H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1H.59C0 13 0 12.59 0 12c0-.59 0-1 .59-1z"></path></svg>
    </button>
  </div>

  <div class="Header-item Header-item--full flex-column flex-lg-row width-full flex-order-2 flex-lg-order-none mr-0 mr-lg-3 mt-3 mt-lg-0 Details-content--hidden">
      <div class="header-search flex-self-stretch flex-lg-self-auto mr-0 mr-lg-3 mb-3 mb-lg-0 scoped-search site-scoped-search js-site-search position-relative js-jump-to"
  role="combobox"
  aria-owns="jump-to-results"
  aria-label="Search or jump to"
  aria-haspopup="listbox"
  aria-expanded="false"
>
  <div class="position-relative">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-site-search-form" role="search" aria-label="Site" data-scope-type="Repository" data-scope-id="164776962" data-scoped-search-url="/Make-School-Courses/CS-1.3-Core-Data-Structures/search" data-unscoped-search-url="/search" action="/Make-School-Courses/CS-1.3-Core-Data-Structures/search" accept-charset="UTF-8" method="get">
      <label class="form-control input-sm header-search-wrapper p-0 header-search-wrapper-jump-to position-relative d-flex flex-justify-between flex-items-center js-chromeless-input-container">
        <input type="text"
          class="form-control input-sm header-search-input jump-to-field js-jump-to-field js-site-search-focus js-site-search-field is-clearable"
          data-hotkey="s,/"
          name="q"
          value=""
          placeholder="Search or jump to…"
          data-unscoped-placeholder="Search or jump to…"
          data-scoped-placeholder="Search or jump to…"
          autocapitalize="off"
          aria-autocomplete="list"
          aria-controls="jump-to-results"
          aria-label="Search or jump to…"
          data-jump-to-suggestions-path="/_graphql/GetSuggestedNavigationDestinations"
          spellcheck="false"
          autocomplete="off"
          >
          <input type="hidden" value="F4AIPQWhHqI0R9UrM3JZ4XcfvkunJxhjapeaHopA/jh+jNegwk8c1n6Ak6QUB74jotToHK0U1bc910RHaWmyOA==" data-csrf="true" class="js-data-jump-to-suggestions-path-csrf" />
          <input type="hidden" class="js-site-search-type-field" name="type" >
            <img src="https://github.githubassets.com/images/search-key-slash.svg" alt="" class="mr-2 header-search-key-slash">

            <div class="Box position-absolute overflow-hidden d-none jump-to-suggestions js-jump-to-suggestions-container">
              
<ul class="d-none js-jump-to-suggestions-template-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-suggestion" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 00-1 1v14a1 1 0 001 1h13a1 1 0 001-1V1a1 1 0 00-1-1z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0013 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 000-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"></path></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

</ul>

<ul class="d-none js-jump-to-no-results-template-container">
  <li class="d-flex flex-justify-center flex-items-center f5 d-none js-jump-to-suggestion p-2">
    <span class="text-gray">No suggested jump to results</span>
  </li>
</ul>

<ul id="jump-to-results" role="listbox" class="p-0 m-0 js-navigation-container jump-to-suggestions-results-container js-jump-to-suggestions-results-container">
  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-scoped-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 00-1 1v14a1 1 0 001 1h13a1 1 0 001-1V1a1 1 0 00-1-1z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0013 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 000-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"></path></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>

  

<li class="d-flex flex-justify-start flex-items-center p-0 f5 navigation-item js-navigation-item js-jump-to-global-search d-none" role="option">
  <a tabindex="-1" class="no-underline d-flex flex-auto flex-items-center jump-to-suggestions-path js-jump-to-suggestion-path js-navigation-open p-2" href="">
    <div class="jump-to-octicon js-jump-to-octicon flex-shrink-0 mr-2 text-center d-none">
      <svg height="16" width="16" class="octicon octicon-repo flex-shrink-0 js-jump-to-octicon-repo d-none" title="Repository" aria-label="Repository" viewBox="0 0 12 16" version="1.1" role="img"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-project flex-shrink-0 js-jump-to-octicon-project d-none" title="Project" aria-label="Project" viewBox="0 0 15 16" version="1.1" role="img"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 00-1 1v14a1 1 0 001 1h13a1 1 0 001-1V1a1 1 0 00-1-1z"></path></svg>
      <svg height="16" width="16" class="octicon octicon-search flex-shrink-0 js-jump-to-octicon-search d-none" title="Search" aria-label="Search" viewBox="0 0 16 16" version="1.1" role="img"><path fill-rule="evenodd" d="M15.7 13.3l-3.81-3.83A5.93 5.93 0 0013 6c0-3.31-2.69-6-6-6S1 2.69 1 6s2.69 6 6 6c1.3 0 2.48-.41 3.47-1.11l3.83 3.81c.19.2.45.3.7.3.25 0 .52-.09.7-.3a.996.996 0 000-1.41v.01zM7 10.7c-2.59 0-4.7-2.11-4.7-4.7 0-2.59 2.11-4.7 4.7-4.7 2.59 0 4.7 2.11 4.7 4.7 0 2.59-2.11 4.7-4.7 4.7z"></path></svg>
    </div>

    <img class="avatar mr-2 flex-shrink-0 js-jump-to-suggestion-avatar d-none" alt="" aria-label="Team" src="" width="28" height="28">

    <div class="jump-to-suggestion-name js-jump-to-suggestion-name flex-auto overflow-hidden text-left no-wrap css-truncate css-truncate-target">
    </div>

    <div class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none js-jump-to-badge-search">
      <span class="js-jump-to-badge-search-text-default d-none" aria-label="in this repository">
        In this repository
      </span>
      <span class="js-jump-to-badge-search-text-global d-none" aria-label="in all of GitHub">
        All GitHub
      </span>
      <span aria-hidden="true" class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>

    <div aria-hidden="true" class="border rounded-1 flex-shrink-0 bg-gray px-1 text-gray-light ml-1 f6 d-none d-on-nav-focus js-jump-to-badge-jump">
      Jump to
      <span class="d-inline-block ml-1 v-align-middle">↵</span>
    </div>
  </a>
</li>


    <li class="d-flex flex-justify-center flex-items-center p-0 f5 js-jump-to-suggestion">
      <img src="https://github.githubassets.com/images/spinners/octocat-spinner-128.gif" alt="Octocat Spinner Icon" class="m-2" width="28">
    </li>
</ul>

            </div>
      </label>
</form>  </div>
</div>


    <nav class="d-flex flex-column flex-lg-row flex-self-stretch flex-lg-self-auto" aria-label="Global">
    <a class="Header-link py-lg-3 d-block d-lg-none py-2 border-top border-lg-top-0 border-white-fade-15" data-ga-click="Header, click, Nav menu - item:dashboard:user" aria-label="Dashboard" href="/dashboard">
      Dashboard
</a>
  <a class="js-selected-navigation-item Header-link py-lg-3  mr-0 mr-lg-3 py-2 border-top border-lg-top-0 border-white-fade-15" data-hotkey="g p" data-ga-click="Header, click, Nav menu - item:pulls context:user" aria-label="Pull requests you created" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls" href="/pulls">
    Pull requests
</a>
  <a class="js-selected-navigation-item Header-link py-lg-3  mr-0 mr-lg-3 py-2 border-top border-lg-top-0 border-white-fade-15" data-hotkey="g i" data-ga-click="Header, click, Nav menu - item:issues context:user" aria-label="Issues you created" data-selected-links="/issues /issues/assigned /issues/mentioned /issues" href="/issues">
    Issues
</a>

    <div class="mr-0 mr-lg-3 py-2 py-lg-0 border-top border-lg-top-0 border-white-fade-15">
      <a class="js-selected-navigation-item Header-link py-lg-3 d-inline-block" data-ga-click="Header, click, Nav menu - item:marketplace context:user" data-octo-click="marketplace_click" data-octo-dimensions="location:nav_bar" data-selected-links=" /marketplace" href="/marketplace">
        Marketplace
</a>      

    </div>

  <a class="js-selected-navigation-item Header-link py-lg-3  mr-0 mr-lg-3 py-2 border-top border-lg-top-0 border-white-fade-15" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship showcases showcases_search showcases_landing /explore" href="/explore">
    Explore
</a>


    <a class="Header-link d-block d-lg-none mr-0 mr-lg-3 py-2 py-lg-3 border-top border-lg-top-0 border-white-fade-15" href="https://github.com/RobotGyal">
      <img class="avatar avatar-user" height="20" width="20" alt="@RobotGyal" src="https://avatars0.githubusercontent.com/u/10855238?s=60&amp;u=3f65f9497b025fa716cd2c7e7629207c3c48288d&amp;v=4" />
      RobotGyal
</a>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form action="/logout" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="kY9YDdqKNmx6WtQ3+/yaPrwUXq9mttl7gCpuNkmPL8Pu3RMG+xKczHh8miAoxc40ckGrAU0n/q2BQa+F43a2gA==" />
      <button type="submit" class="Header-link mr-0 mr-lg-3 py-2 py-lg-3 border-top border-lg-top-0 border-white-fade-15 d-lg-none btn-link d-block width-full text-left" data-ga-click="Header, sign out, icon:logout" style="padding-left: 2px;">
        <svg class="octicon octicon-sign-out v-align-middle" viewBox="0 0 16 17" version="1.1" width="16" height="17" aria-hidden="true"><path fill-rule="evenodd" d="M12 9V7H8V5h4V3l4 3-4 3zm-2 3H6V3L2 1h8v3h1V1c0-.55-.45-1-1-1H1C.45 0 0 .45 0 1v11.38c0 .39.22.73.55.91L6 16.01V13h4c.55 0 1-.45 1-1V8h-1v4z"></path></svg>
        Sign out
      </button>
</form></nav>

  </div>

  <div class="Header-item Header-item--full flex-justify-center d-lg-none position-relative">
    <div class="css-truncate css-truncate-target width-fit position-absolute left-0 right-0 text-center">
                <svg class="octicon octicon-repo" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"></path></svg>
    <a class="Header-link" href="/Make-School-Courses">Make-School-Courses</a>
    /
    <a class="Header-link" href="/Make-School-Courses/CS-1.3-Core-Data-Structures">CS-1.3-Core-Data-Structures</a>

</div>
  </div>

  <div class="Header-item mr-0 mr-lg-3 flex-order-1 flex-lg-order-none">
    
    <a aria-label="You have unread notifications" class="Header-link notification-indicator position-relative tooltipped tooltipped-sw js-socket-channel js-notification-indicator" data-hotkey="g n" data-ga-click="Header, go to notifications, icon:unread" data-channel="notification-changed:10855238" href="/notifications">
        <span class="js-indicator-modifier mail-status unread"></span>
        <svg class="octicon octicon-bell" viewBox="0 0 15 16" version="1.1" width="15" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 12v1H0v-1l.73-.58c.77-.77.81-2.55 1.19-4.42C2.69 3.23 6 2 6 2c0-.55.45-1 1-1s1 .45 1 1c0 0 3.39 1.23 4.16 5 .38 1.88.42 3.66 1.19 4.42l.66.58H14zm-7 4c1.11 0 2-.89 2-2H5c0 1.11.89 2 2 2z"></path></svg>
</a>
  </div>


  <div class="Header-item position-relative d-none d-lg-flex">
    <details class="details-overlay details-reset">
  <summary class="Header-link"
      aria-label="Create new…"
      data-ga-click="Header, create new, icon:add">
    <svg class="octicon octicon-plus" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 9H7v5H5V9H0V7h5V2h2v5h5v2z"></path></svg> <span class="dropdown-caret"></span>
  </summary>
  <details-menu class="dropdown-menu dropdown-menu-sw mt-n2">
    
<a role="menuitem" class="dropdown-item" href="/new" data-ga-click="Header, create new repository">
  New repository
</a>

  <a role="menuitem" class="dropdown-item" href="/new/import" data-ga-click="Header, import a repository">
    Import repository
  </a>

<a role="menuitem" class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, create new gist">
  New gist
</a>

  <a role="menuitem" class="dropdown-item" href="/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>


  <div role="none" class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="Make-School-Courses/CS-1.3-Core-Data-Structures">This repository</span>
  </div>
    <a role="menuitem" class="dropdown-item" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/issues/new/choose" data-ga-click="Header, create new issue" data-skip-pjax>
      New issue
    </a>


  </details-menu>
</details>

  </div>

  <div class="Header-item position-relative mr-0 d-none d-lg-flex">
    
  <details class="details-overlay details-reset js-feature-preview-indicator-container" data-feature-preview-indicator-src="/users/RobotGyal/feature_preview/indicator_check">

  <summary class="Header-link"
    aria-label="View profile and more"
    data-ga-click="Header, show menu, icon:avatar">
    <img
  alt="@RobotGyal"
  width="20"
  height="20"
  src="https://avatars0.githubusercontent.com/u/10855238?s=60&amp;u=3f65f9497b025fa716cd2c7e7629207c3c48288d&amp;v=4"
  class="avatar avatar-user " />

      <span class="feature-preview-indicator js-feature-preview-indicator" hidden></span>
    <span class="dropdown-caret"></span>
  </summary>
  <details-menu class="dropdown-menu dropdown-menu-sw mt-n2" style="width: 180px">
    <div class="header-nav-current-user css-truncate"><a role="menuitem" class="no-underline user-profile-link px-3 pt-2 pb-2 mb-n2 mt-n1 d-block" href="/RobotGyal" data-ga-click="Header, go to profile, text:Signed in as">Signed in as <strong class="css-truncate-target">RobotGyal</strong></a></div>
    <div role="none" class="dropdown-divider"></div>

      <div class="pl-3 pr-3 f6 user-status-container js-user-status-context pb-1" data-url="/users/status?compact=1&amp;link_mentions=0&amp;truncate=1">
        
<div class="js-user-status-container
    user-status-compact rounded-1 px-2 py-1 mt-2
    border
  " data-team-hovercards-enabled>
  <details class="js-user-status-details details-reset details-overlay details-overlay-dark">
    <summary class="btn-link btn-block link-gray no-underline js-toggle-user-status-edit toggle-user-status-edit "
      role="menuitem" data-hydro-click="{&quot;event_type&quot;:&quot;user_profile.click&quot;,&quot;payload&quot;:{&quot;profile_user_id&quot;:26469999,&quot;target&quot;:&quot;EDIT_USER_STATUS&quot;,&quot;user_id&quot;:10855238,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;}}" data-hydro-click-hmac="66e4a4ba01daa2190df820519ec0f9aad926e8682cd1751d3af25c6f1de4c8ff">
      <div class="d-flex">
        <div class="f6 lh-condensed user-status-header
          d-inline-block v-align-middle
            user-status-emoji-only-header circle
            pr-2
"
            style="max-width: 29px"
          >
          <div class="user-status-emoji-container flex-shrink-0 mr-1  lh-condensed-ultra v-align-bottom" style="margin-top: 2px;">
            <div><g-emoji class="g-emoji" alias="bulb" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4a1.png">💡</g-emoji></div>
          </div>
        </div>
        <div class="
          d-inline-block v-align-middle
          
          
           css-truncate css-truncate-target 
           user-status-message-wrapper f6"
           style="line-height: 20px;" >
          <div class="d-inline-block text-gray-dark v-align-text-top text-left">
                <span>Innovating</span>
          </div>
        </div>
      </div>
    </summary>
    <details-dialog class="details-dialog rounded-1 anim-fade-in fast Box Box--overlay" role="dialog" tabindex="-1">
      <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="position-relative flex-auto js-user-status-form" action="/users/status?compact=1&amp;link_mentions=0&amp;truncate=1" accept-charset="UTF-8" method="post"><input type="hidden" name="_method" value="put" /><input type="hidden" name="authenticity_token" value="EBIyRSZ8SVtRzr3kA3qutc5Qqm3+mKQoiG9Anne/mdLmARB1ivTkijdGneP4FFF/3dVrMR7sBL3BwZ1I1HDGZQ==" />
        <div class="Box-header bg-gray border-bottom p-3">
          <button class="Box-btn-octicon js-toggle-user-status-edit btn-octicon float-right" type="reset" aria-label="Close dialog" data-close-dialog>
            <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"></path></svg>
          </button>
          <h3 class="Box-title f5 text-bold text-gray-dark">Edit status</h3>
        </div>
        <input type="hidden" name="emoji" class="js-user-status-emoji-field" value=":bulb:">
        <input type="hidden" name="organization_id" class="js-user-status-org-id-field" value="">
        <div class="px-3 py-2 text-gray-dark">
          <div class="js-characters-remaining-container position-relative mt-2">
            <div class="input-group d-table form-group my-0 js-user-status-form-group">
              <span class="input-group-button d-table-cell v-align-middle" style="width: 1%">
                <button type="button" aria-label="Choose an emoji" class="btn-outline btn js-toggle-user-status-emoji-picker btn-open-emoji-picker p-0">
                  <span class="js-user-status-original-emoji" hidden><div><g-emoji class="g-emoji" alias="bulb" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4a1.png">💡</g-emoji></div></span>
                  <span class="js-user-status-custom-emoji"><div><g-emoji class="g-emoji" alias="bulb" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f4a1.png">💡</g-emoji></div></span>
                  <span class="js-user-status-no-emoji-icon" hidden>
                    <svg class="octicon octicon-smiley" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8s3.58 8 8 8 8-3.58 8-8-3.58-8-8-8zm4.81 12.81a6.72 6.72 0 01-2.17 1.45c-.83.36-1.72.53-2.64.53-.92 0-1.81-.17-2.64-.53-.81-.34-1.55-.83-2.17-1.45a6.773 6.773 0 01-1.45-2.17A6.59 6.59 0 011.21 8c0-.92.17-1.81.53-2.64.34-.81.83-1.55 1.45-2.17.62-.62 1.36-1.11 2.17-1.45A6.59 6.59 0 018 1.21c.92 0 1.81.17 2.64.53.81.34 1.55.83 2.17 1.45.62.62 1.11 1.36 1.45 2.17.36.83.53 1.72.53 2.64 0 .92-.17 1.81-.53 2.64-.34.81-.83 1.55-1.45 2.17zM4 6.8v-.59c0-.66.53-1.19 1.2-1.19h.59c.66 0 1.19.53 1.19 1.19v.59c0 .67-.53 1.2-1.19 1.2H5.2C4.53 8 4 7.47 4 6.8zm5 0v-.59c0-.66.53-1.19 1.2-1.19h.59c.66 0 1.19.53 1.19 1.19v.59c0 .67-.53 1.2-1.19 1.2h-.59C9.53 8 9 7.47 9 6.8zm4 3.2c-.72 1.88-2.91 3-5 3s-4.28-1.13-5-3c-.14-.39.23-1 .66-1h8.59c.41 0 .89.61.75 1z"></path></svg>
                  </span>
                </button>
              </span>
              <text-expander keys=": @" data-mention-url="/autocomplete/user-suggestions" data-emoji-url="/autocomplete/emoji">
                <input
                  type="text"
                  autocomplete="off"
                  data-no-org-url="/autocomplete/user-suggestions"
                  data-org-url="/suggestions?mention_suggester=1"
                  data-maxlength="80"
                  class="d-table-cell width-full form-control js-user-status-message-field js-characters-remaining-field"
                  placeholder="What's happening?"
                  name="message"
                  value="Innovating"
                  aria-label="What is your current status?">
              </text-expander>
              <div class="error">Could not update your status, please try again.</div>
            </div>
            <div style="margin-left: 53px" class="my-1 text-small label-characters-remaining js-characters-remaining" data-suffix="remaining" hidden>
              80 remaining
            </div>
          </div>
          <include-fragment class="js-user-status-emoji-picker" data-url="/users/status/emoji"></include-fragment>
          <div class="overflow-auto ml-n3 mr-n3 px-3 border-bottom" style="max-height: 33vh">
            <div class="user-status-suggestions js-user-status-suggestions collapsed overflow-hidden">
              <h4 class="f6 text-normal my-3">Suggestions:</h4>
              <div class="mx-3 mt-2 clearfix">
                  <div class="float-left col-6">
                      <button type="button" value=":palm_tree:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="palm_tree" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f334.png">🌴</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          On vacation
                        </div>
                      </button>
                      <button type="button" value=":face_with_thermometer:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="face_with_thermometer" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f912.png">🤒</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          Out sick
                        </div>
                      </button>
                  </div>
                  <div class="float-left col-6">
                      <button type="button" value=":house:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="house" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f3e0.png">🏠</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          Working from home
                        </div>
                      </button>
                      <button type="button" value=":dart:" class="d-flex flex-items-baseline flex-items-stretch lh-condensed f6 btn-link link-gray no-underline js-predefined-user-status mb-1">
                        <div class="emoji-status-width mr-2 v-align-middle js-predefined-user-status-emoji">
                          <g-emoji alias="dart" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/1f3af.png">🎯</g-emoji>
                        </div>
                        <div class="d-flex flex-items-center no-underline js-predefined-user-status-message ws-normal text-left" style="border-left: 1px solid transparent">
                          Focusing
                        </div>
                      </button>
                  </div>
              </div>
            </div>
            <div class="user-status-limited-availability-container">
              <div class="form-checkbox my-0">
                <input type="checkbox" name="limited_availability" value="1" class="js-user-status-limited-availability-checkbox" data-default-message="I may be slow to respond." aria-describedby="limited-availability-help-text-truncate-true-compact-true" id="limited-availability-truncate-true-compact-true">
                <label class="d-block f5 text-gray-dark mb-1" for="limited-availability-truncate-true-compact-true">
                  Busy
                </label>
                <p class="note" id="limited-availability-help-text-truncate-true-compact-true">
                  When others mention you, assign you, or request your review,
                  GitHub will let them know that you have limited availability.
                </p>
              </div>
            </div>
          </div>
          <div class="d-inline-block f5 mr-2 pt-3 pb-2" >
  <div class="d-inline-block mr-1">
    Clear status
  </div>

  <details class="js-user-status-expire-drop-down f6 dropdown details-reset details-overlay d-inline-block mr-2">
    <summary class="f5 btn-link link-gray-dark border px-2 py-1 rounded-1" aria-haspopup="true">
      <div class="js-user-status-expiration-interval-selected d-inline-block v-align-baseline">
        Never
      </div>
      <div class="dropdown-caret"></div>
    </summary>

    <ul class="dropdown-menu dropdown-menu-se pl-0 overflow-auto" style="width: 220px; max-height: 15.5em">
      <li>
        <button type="button" class="btn-link dropdown-item js-user-status-expire-button ws-normal" title="Never">
          <span class="d-inline-block text-bold mb-1">Never</span>
          <div class="f6 lh-condensed">Keep this status until you clear your status or edit your status.</div>
        </button>
      </li>
      <li class="dropdown-divider" role="none"></li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="in 30 minutes" value="2020-04-28T18:06:49-07:00">
            in 30 minutes
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="in 1 hour" value="2020-04-28T18:36:49-07:00">
            in 1 hour
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="in 4 hours" value="2020-04-28T21:36:49-07:00">
            in 4 hours
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="today" value="2020-04-28T23:59:59-07:00">
            today
          </button>
        </li>
        <li>
          <button type="button" class="btn-link dropdown-item ws-normal js-user-status-expire-button" title="this week" value="2020-05-03T23:59:59-07:00">
            this week
          </button>
        </li>
    </ul>
  </details>
  <input class="js-user-status-expiration-date-input" type="hidden" name="expires_at" value="">
</div>

          <include-fragment class="js-user-status-org-picker" data-url="/users/status/organizations"></include-fragment>
        </div>
        <div class="d-flex flex-items-center flex-justify-between p-3 border-top">
          <button type="submit"  class="width-full btn btn-primary mr-2 js-user-status-submit">
            Set status
          </button>
          <button type="button"  class="width-full js-clear-user-status-button btn ml-2 js-user-status-exists">
            Clear status
          </button>
        </div>
</form>    </details-dialog>
  </details>
</div>

      </div>
      <div role="none" class="dropdown-divider"></div>

    <a role="menuitem" class="dropdown-item" href="/RobotGyal" data-ga-click="Header, go to profile, text:your profile">Your profile</a>

    <a role="menuitem" class="dropdown-item" href="/RobotGyal?tab=repositories" data-ga-click="Header, go to repositories, text:your repositories">Your repositories</a>

    <a role="menuitem" class="dropdown-item" href="/RobotGyal?tab=projects" data-ga-click="Header, go to projects, text:your projects">Your projects</a>

    <a role="menuitem" class="dropdown-item" href="/RobotGyal?tab=stars" data-ga-click="Header, go to starred repos, text:your stars">Your stars</a>
      <a role="menuitem" class="dropdown-item" href="https://gist.github.com/mine" data-ga-click="Header, your gists, text:your gists">Your gists</a>





    <div role="none" class="dropdown-divider"></div>
      
<div id="feature-enrollment-toggle" class="hide-sm hide-md feature-preview-details position-relative">
  <button
    type="button"
    class="dropdown-item btn-link"
    role="menuitem"
    data-feature-preview-trigger-url="/users/RobotGyal/feature_previews"
    data-feature-preview-close-details="{&quot;event_type&quot;:&quot;feature_preview.clicks.close_modal&quot;,&quot;payload&quot;:{&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}"
    data-feature-preview-close-hmac="988aaa55970029d863476294127299a0f8c20c319eabc3ca964b3baa1aad1d6e"
    data-hydro-click="{&quot;event_type&quot;:&quot;feature_preview.clicks.open_modal&quot;,&quot;payload&quot;:{&quot;link_location&quot;:&quot;user_dropdown&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}"
    data-hydro-click-hmac="e5a05915f5a47c6537ad2486b3d2770586b2bfc55b407883dd8efdecfa772919"
  >
    Feature preview
  </button>
    <span class="feature-preview-indicator js-feature-preview-indicator" hidden></span>
</div>

    <a role="menuitem" class="dropdown-item" href="https://help.github.com" data-ga-click="Header, go to help, text:help">Help</a>
    <a role="menuitem" class="dropdown-item" href="/settings/profile" data-ga-click="Header, go to settings, icon:settings">Settings</a>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="logout-form" action="/logout" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="NaUlktxYrnN+JqKA1a667b45BgP/6ZCvfceuB+cfgetK926Z/cAE03wA7JcGl+7ncGzzrdR4t3l8rG+0TeYYqA==" />
      
      <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout" role="menuitem">
        Sign out
      </button>
      <input type="text" name="required_field_3476" hidden="hidden" class="form-control" /><input type="hidden" name="timestamp" value="1588120609015" class="form-control" /><input type="hidden" name="timestamp_secret" value="98d237864f970cf8f0c7a59c75c789b378da0bed4e3fb14fc2fa44efef94679e" class="form-control" />
</form>  </details-menu>
</details>

  </div>

</header>

        

    </div>

  <div id="start-of-content" class="show-on-focus"></div>




    <div id="js-flash-container">


  <template class="js-flash-template">
    <div class="flash flash-full  js-flash-template-container">
  <div class="container-lg px-2" >
    <button class="flash-close js-flash-close" type="button" aria-label="Dismiss this message">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"></path></svg>
    </button>
    
      <div class="js-flash-template-message"></div>

  </div>
</div>
  </template>
</div>


      

  <include-fragment class="js-notification-shelf-include-fragment" data-base-src="https://github.com/notifications/beta/shelf"></include-fragment>




  <div class="application-main " data-commit-hovercards-enabled>
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <main  >
      

  




  









  <div class="pagehead repohead hx_repohead readability-menu bg-gray-light pb-0 pt-0 pt-lg-3">

    <div class="d-flex container-lg mb-4 p-responsive d-none d-lg-flex">

      <div class="flex-auto min-width-0 width-fit mr-3">
        <h1 class="public  d-flex flex-wrap flex-items-center break-word float-none ">
  <span class="flex-self-stretch" style="margin-top: -2px;">
      <svg class="octicon octicon-repo" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"></path></svg>
  </span>
  <span class="author ml-2 flex-self-stretch" itemprop="author">
    <a class="url fn" rel="author" data-hovercard-type="organization" data-hovercard-url="/orgs/Make-School-Courses/hovercard" href="/Make-School-Courses">Make-School-Courses</a>
  </span>
  <span class="path-divider flex-self-stretch">/</span>
  <strong itemprop="name" class="mr-2 flex-self-stretch">
    <a data-pjax="#js-repo-pjax-container" href="/Make-School-Courses/CS-1.3-Core-Data-Structures">CS-1.3-Core-Data-Structures</a>
  </strong>
  
</h1>


      </div>

      <ul class="pagehead-actions flex-shrink-0 " >



    <li hidden>
      <include-fragment src="/Make-School-Courses/CS-1.3-Core-Data-Structures/used_by_count" accept="text/fragment+html">
</include-fragment>
    </li>

  <li>
    
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form data-remote="true" class="clearfix js-social-form js-social-container" action="/notifications/subscribe" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="EzXgn9jgRVlLkoIg3OWubEHeVoa07pGoeIhznKJ0XpqTQa/dh/g1NygHucHSXv3PfNDWxNby0B+8kVhn4bneGQ==" />      <input type="hidden" name="repository_id" value="164776962">

      <details class="details-reset details-overlay select-menu float-left">
        <summary class="select-menu-button float-left btn btn-sm btn-with-count" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;WATCH_BUTTON&quot;,&quot;repository_id&quot;:164776962,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="70f95279f9e2eb766c592eef1e6ba3ebb3c61a7e0533ed2d12ef83fafb2e39b4" data-ga-click="Repository, click Watch settings, action:blob#show">          <span data-menu-button>
              <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"></path></svg>
              Watch
          </span>
</summary>        <details-menu
          class="select-menu-modal position-absolute mt-5"
          style="z-index: 99;">
          <div class="select-menu-header">
            <span class="select-menu-title">Notifications</span>
          </div>
          <div class="select-menu-list">
            <button type="submit" name="do" value="included" class="select-menu-item width-full" aria-checked="true" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Not watching</span>
                <span class="description">Be notified only when participating or @mentioned.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"></path></svg>
                  Watch
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="release_only" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Releases only</span>
                <span class="description">Be notified of new releases, and when participating or @mentioned.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"></path></svg>
                  Unwatch releases
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="subscribed" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Watching</span>
                <span class="description">Be notified of all conversations.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-eye v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"></path></svg>
                  Unwatch
                </span>
              </div>
            </button>

            <button type="submit" name="do" value="ignore" class="select-menu-item width-full" aria-checked="false" role="menuitemradio">
              <svg class="octicon octicon-check select-menu-item-icon" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
              <div class="select-menu-item-text">
                <span class="select-menu-item-heading">Ignoring</span>
                <span class="description">Never be notified.</span>
                <span class="hidden-select-button-text" data-menu-button-contents>
                  <svg class="octicon octicon-mute v-align-text-bottom" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 2.81v10.38c0 .67-.81 1-1.28.53L3 10H1c-.55 0-1-.45-1-1V7c0-.55.45-1 1-1h2l3.72-3.72C7.19 1.81 8 2.14 8 2.81zm7.53 3.22l-1.06-1.06-1.97 1.97-1.97-1.97-1.06 1.06L11.44 8 9.47 9.97l1.06 1.06 1.97-1.97 1.97 1.97 1.06-1.06L13.56 8l1.97-1.97z"></path></svg>
                  Stop ignoring
                </span>
              </div>
            </button>
          </div>
        </details-menu>
      </details>
        <a class="social-count js-social-count"
          href="/Make-School-Courses/CS-1.3-Core-Data-Structures/watchers"
          aria-label="5 users are watching this repository">
          5
        </a>
</form>
  </li>

  <li>
      <div class="js-toggler-container js-social-container starring-container ">
    <form class="starred js-social-form" action="/Make-School-Courses/CS-1.3-Core-Data-Structures/unstar" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="mdD2iR5nKlJfZMhfQQMqwpoCKoczn2X3IoXulylWGYUUvrr9zWr8QGZZVmwHxrKGb5uJ5H0Znl71fPn2BaSUEw==" />
      <input type="hidden" name="context" value="repository"></input>
      <button type="submit" class="btn btn-sm btn-with-count js-toggler-target" aria-label="Unstar this repository" title="Unstar Make-School-Courses/CS-1.3-Core-Data-Structures" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;UNSTAR_BUTTON&quot;,&quot;repository_id&quot;:164776962,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="d96f8a8ef92e324c3ca3fff895fc4b76ea4c625aa3a0134eb0f49939b3c6f7e1" data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">        <svg height="16" class="octicon octicon-star v-align-text-bottom" vertical_align="text_bottom" viewBox="0 0 14 16" version="1.1" width="14" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"></path></svg>

        Unstar
</button>        <a class="social-count js-social-count" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/stargazers"
           aria-label="11 users starred this repository">
           11
        </a>
</form>
    <form class="unstarred js-social-form" action="/Make-School-Courses/CS-1.3-Core-Data-Structures/star" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="NzoCkCN3zccg989miIXvcYnLj2QgoaOSMS60acFwut7xaEbawy/4M4efC3CFSFWoEZcDbFs9V3Cog0QpwEUBuA==" />
      <input type="hidden" name="context" value="repository"></input>
      <button type="submit" class="btn btn-sm btn-with-count js-toggler-target" aria-label="Unstar this repository" title="Star Make-School-Courses/CS-1.3-Core-Data-Structures" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;STAR_BUTTON&quot;,&quot;repository_id&quot;:164776962,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="ff950f4120d2f7fefd43fe706ecdd3fb08e8744d0399352b05650c06ccaf8de4" data-ga-click="Repository, click star button, action:blob#show; text:Star">        <svg height="16" class="octicon octicon-star v-align-text-bottom" vertical_align="text_bottom" viewBox="0 0 14 16" version="1.1" width="14" aria-hidden="true"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74L14 6z"></path></svg>

        Star
</button>        <a class="social-count js-social-count" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/stargazers"
           aria-label="11 users starred this repository">
          11
        </a>
</form>  </div>

  </li>

  <li>
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="btn-with-count" action="/Make-School-Courses/CS-1.3-Core-Data-Structures/fork" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="71G7WQRQG7FF16wvSwtLX6EWcHhoQz3DJWCw/zIJrI8/74BKZN/NVySC7Fxiwjm3XDGWu+jrZ6usdyv1HMHIkg==" />
            <button class="btn btn-sm btn-with-count" data-hydro-click="{&quot;event_type&quot;:&quot;repository.click&quot;,&quot;payload&quot;:{&quot;target&quot;:&quot;FORK_BUTTON&quot;,&quot;repository_id&quot;:164776962,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="935aea12fe95cd802b1ab1b9248c81fbdfa3157e10fd54161ea0f334823ed424" data-ga-click="Repository, show fork modal, action:blob#show; text:Fork" type="submit" title="Fork your own copy of Make-School-Courses/CS-1.3-Core-Data-Structures to your account" aria-label="Fork your own copy of Make-School-Courses/CS-1.3-Core-Data-Structures to your account">              <svg class="octicon octicon-repo-forked v-align-text-bottom" viewBox="0 0 10 16" version="1.1" width="10" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 00-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 002 1a1.993 1.993 0 00-1 3.72V6.5l3 3v1.78A1.993 1.993 0 005 15a1.993 1.993 0 001-3.72V9.5l3-3V4.72A1.993 1.993 0 008 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
              Fork
</button></form>
    <a href="/Make-School-Courses/CS-1.3-Core-Data-Structures/network/members" class="social-count"
       aria-label="34 users forked this repository">
      34
    </a>
  </li>
</ul>

    </div>
      <nav class="js-repo-nav js-sidenav-container-pjax clearfix hx_reponav reponav p-responsive d-none d-lg-block container-lg"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
    aria-label="Repository"
     data-pjax="#js-repo-pjax-container">
  <ul class="list-style-none">
    <li  itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a class="js-selected-navigation-item selected reponav-item" itemprop="url" data-hotkey="g c" aria-current="page" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /Make-School-Courses/CS-1.3-Core-Data-Structures" href="/Make-School-Courses/CS-1.3-Core-Data-Structures">
        <div class="d-inline"><svg class="octicon octicon-code" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"></path></svg></div>
        <span itemprop="name">Code</span>
        <meta itemprop="position" content="1">
</a>    </li>

      <li  itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" data-hotkey="g i" class="js-selected-navigation-item reponav-item" data-selected-links="repo_issues repo_labels repo_milestones /Make-School-Courses/CS-1.3-Core-Data-Structures/issues" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/issues">
          <div class="d-inline"><svg class="octicon octicon-issue-opened" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 011.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg></div>
          <span itemprop="name">Issues</span>
          <span class="Counter">1</span>
          <meta itemprop="position" content="2">
</a>      </li>

    <li  itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a data-hotkey="g p" data-skip-pjax="true" itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /Make-School-Courses/CS-1.3-Core-Data-Structures/pulls" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/pulls">
        <div class="d-inline"><svg class="octicon octicon-git-pull-request" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0010 15a1.993 1.993 0 001-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 00-1 3.72v6.56A1.993 1.993 0 002 15a1.993 1.993 0 001-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg></div>
        <span itemprop="name">Pull requests</span>
        <span class="Counter">0</span>
        <meta itemprop="position" content="4">
</a>    </li>


      <li itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement" class="position-relative float-left ">
        <a data-hotkey="g w" data-skip-pjax="true" class="js-selected-navigation-item reponav-item" data-selected-links="repo_actions /Make-School-Courses/CS-1.3-Core-Data-Structures/actions" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/actions">
          <div class="d-inline"><svg class="octicon octicon-play" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M14 8A7 7 0 110 8a7 7 0 0114 0zm-8.223 3.482l4.599-3.066a.5.5 0 000-.832L5.777 4.518A.5.5 0 005 4.934v6.132a.5.5 0 00.777.416z"></path></svg></div>
          Actions
</a>
      </li>

      <li >
        <a data-hotkey="g b" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /Make-School-Courses/CS-1.3-Core-Data-Structures/projects" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/projects">
          <div class="d-inline"><svg class="octicon octicon-project" viewBox="0 0 15 16" version="1.1" width="15" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 00-1 1v14a1 1 0 001 1h13a1 1 0 001-1V1a1 1 0 00-1-1z"></path></svg></div>
          Projects
          <span class="Counter">0</span>
</a>      </li>

      <li >
        <a class="js-selected-navigation-item reponav-item" data-hotkey="g w" data-selected-links="repo_wiki /Make-School-Courses/CS-1.3-Core-Data-Structures/wiki" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/wiki">
          <div class="d-inline"><svg class="octicon octicon-book" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M3 5h4v1H3V5zm0 3h4V7H3v1zm0 2h4V9H3v1zm11-5h-4v1h4V5zm0 2h-4v1h4V7zm0 2h-4v1h4V9zm2-6v9c0 .55-.45 1-1 1H9.5l-1 1-1-1H2c-.55 0-1-.45-1-1V3c0-.55.45-1 1-1h5.5l1 1 1-1H15c.55 0 1 .45 1 1zm-8 .5L7.5 3H2v9h6V3.5zm7-.5H9.5l-.5.5V12h6V3z"></path></svg></div>
          Wiki
</a>      </li>

      <li >
        <a data-skip-pjax="true" class="js-selected-navigation-item reponav-item" data-selected-links="security overview alerts policy token_scanning code_scanning /Make-School-Courses/CS-1.3-Core-Data-Structures/security" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/security">
          <div class="d-inline"><svg class="octicon octicon-shield" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 2l7-2 7 2v6.02C14 12.69 8.69 16 7 16c-1.69 0-7-3.31-7-7.98V2zm1 .75L7 1l6 1.75v5.268C13 12.104 8.449 15 7 15c-1.449 0-6-2.896-6-6.982V2.75zm1 .75L7 2v12c-1.207 0-5-2.482-5-5.985V3.5z"></path></svg></div>
          Security
              <span class="Counter js-security-tab-count" data-url="/Make-School-Courses/CS-1.3-Core-Data-Structures/security/overall-count" hidden></span>
</a>      </li>

      <li >
        <a class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors dependency_graph dependabot_updates pulse people /Make-School-Courses/CS-1.3-Core-Data-Structures/pulse" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/pulse">
          <div class="d-inline"><svg class="octicon octicon-graph" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"></path></svg></div>
          Insights
</a>      </li>


  </ul>
</nav>

  <div class="reponav-wrapper reponav-small d-lg-none">
  <nav class="reponav js-reponav text-center no-wrap"
       itemscope
       itemtype="http://schema.org/BreadcrumbList">

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a class="js-selected-navigation-item selected reponav-item" itemprop="url" aria-current="page" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /Make-School-Courses/CS-1.3-Core-Data-Structures" href="/Make-School-Courses/CS-1.3-Core-Data-Structures">
        <span itemprop="name">Code</span>
        <meta itemprop="position" content="1">
</a>    </span>

      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_issues repo_labels repo_milestones /Make-School-Courses/CS-1.3-Core-Data-Structures/issues" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/issues">
          <span itemprop="name">Issues</span>
          <span class="Counter">1</span>
          <meta itemprop="position" content="2">
</a>      </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_pulls checks /Make-School-Courses/CS-1.3-Core-Data-Structures/pulls" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/pulls">
        <span itemprop="name">Pull requests</span>
        <span class="Counter">0</span>
        <meta itemprop="position" content="4">
</a>    </span>


      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /Make-School-Courses/CS-1.3-Core-Data-Structures/projects" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/projects">
          <span itemprop="name">Projects</span>
          <span class="Counter">0</span>
          <meta itemprop="position" content="5">
</a>      </span>

      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_actions /Make-School-Courses/CS-1.3-Core-Data-Structures/actions" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/actions">
          <span itemprop="name">Actions</span>
          <meta itemprop="position" content="6">
</a>      </span>

      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="repo_wiki /Make-School-Courses/CS-1.3-Core-Data-Structures/wiki" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/wiki">
          <span itemprop="name">Wiki</span>
          <meta itemprop="position" content="7">
</a>      </span>

      <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="security overview alerts policy token_scanning code_scanning /Make-School-Courses/CS-1.3-Core-Data-Structures/security" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/security">
        <span itemprop="name">Security</span>
            <span class="Counter js-security-deferred-tab-count" hidden></span>
        <meta itemprop="position" content="8">
</a>
      <a class="js-selected-navigation-item reponav-item" data-selected-links="pulse /Make-School-Courses/CS-1.3-Core-Data-Structures/pulse" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/pulse">
        Pulse
</a>
      <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
        <a itemprop="url" class="js-selected-navigation-item reponav-item" data-selected-links="community /Make-School-Courses/CS-1.3-Core-Data-Structures/community" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/community">
          Community
</a>      </span>

  </nav>
</div>


  </div>

  

  <include-fragment class="js-notification-shelf-include-fragment" data-base-src="https://github.com/notifications/beta/shelf"></include-fragment>


<div class="container-lg clearfix new-discussion-timeline  p-responsive">
  <div class="repository-content ">

    
    

  


    <a class="d-none js-permalink-shortcut" data-hotkey="y" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/9c4c60e3227c913bb528f8cbb57fc3fb75561711/Code/linked-list/linkedlist_test.py">Permalink</a>

    <!-- blob contrib key: blob_contributors:v22:1bc30cb559dfe28dce51c2f6cbd471d1 -->
    

    <div class="d-flex flex-items-start flex-shrink-0 flex-column flex-md-row pb-3">
      <span class="d-flex flex-justify-between width-full width-md-auto">
        
<details class="details-reset details-overlay branch-select-menu " id="branch-select-menu">
  <summary class="btn css-truncate btn-sm"
           data-hotkey="w"
           title="Switch branches or tags">
    <i>Branch:</i>
    <span class="css-truncate-target" data-menu-button>master</span>
    <span class="dropdown-caret"></span>
  </summary>

  <details-menu class="SelectMenu SelectMenu--hasFilter" src="/Make-School-Courses/CS-1.3-Core-Data-Structures/refs/master/Code/linked-list/linkedlist_test.py?source_action=show&amp;source_controller=blob" preload>
    <div class="SelectMenu-modal">
      <include-fragment class="SelectMenu-loading" aria-label="Menu is loading">
        <svg class="octicon octicon-octoface anim-pulse" height="32" viewBox="0 0 16 16" version="1.1" width="32" aria-hidden="true"><path fill-rule="evenodd" d="M14.7 5.34c.13-.32.55-1.59-.13-3.31 0 0-1.05-.33-3.44 1.3-1-.28-2.07-.32-3.13-.32s-2.13.04-3.13.32c-2.39-1.64-3.44-1.3-3.44-1.3-.68 1.72-.26 2.99-.13 3.31C.49 6.21 0 7.33 0 8.69 0 13.84 3.33 15 7.98 15S16 13.84 16 8.69c0-1.36-.49-2.48-1.3-3.35zM8 14.02c-3.3 0-5.98-.15-5.98-3.35 0-.76.38-1.48 1.02-2.07 1.07-.98 2.9-.46 4.96-.46 2.07 0 3.88-.52 4.96.46.65.59 1.02 1.3 1.02 2.07 0 3.19-2.68 3.35-5.98 3.35zM5.49 9.01c-.66 0-1.2.8-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.54-1.78-1.2-1.78zm5.02 0c-.66 0-1.2.79-1.2 1.78s.54 1.79 1.2 1.79c.66 0 1.2-.8 1.2-1.79s-.53-1.78-1.2-1.78z"></path></svg>
      </include-fragment>
    </div>
  </details-menu>
</details>

        <div class="BtnGroup flex-shrink-0 d-md-none">
          <a href="/Make-School-Courses/CS-1.3-Core-Data-Structures/find/master"
                class="js-pjax-capture-input btn btn-sm BtnGroup-item"
                data-pjax
                data-hotkey="t">
            Find file
          </a>
          <clipboard-copy value="Code/linked-list/linkedlist_test.py" class="btn btn-sm BtnGroup-item">
            Copy path
          </clipboard-copy>
        </div>
      </span>
      <h2 id="blob-path" class="breadcrumb flex-auto min-width-0 text-normal flex-md-self-center ml-md-2 mr-md-3 my-2 my-md-0">
        <span class="js-repo-root text-bold"><span class="js-path-segment"><a data-pjax="true" href="/Make-School-Courses/CS-1.3-Core-Data-Structures"><span>CS-1.3-Core-Data-Structures</span></a></span></span><span class="separator">/</span><span class="js-path-segment"><a data-pjax="true" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/tree/master/Code"><span>Code</span></a></span><span class="separator">/</span><span class="js-path-segment"><a data-pjax="true" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/tree/master/Code/linked-list"><span>linked-list</span></a></span><span class="separator">/</span><strong class="final-path">linkedlist_test.py</strong>
          <span class="separator">/</span><details class="details-reset details-overlay d-inline" id="jumpto-symbol-select-menu">
  <summary class="btn-link link-gray css-truncate" aria-haspopup="true" data-hotkey="r" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.click_on_blob_definitions&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;click_on_blob_definitions&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="c07a5d5af2b080336521dc749fe9bd36724a8b582ce91904129be045294441d4">
      <svg class="octicon octicon-code" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"></path></svg>
    <span data-menu-button>Jump to</span>
    <span class="dropdown-caret"></span>
  </summary>
  <details-menu class="SelectMenu SelectMenu--hasFilter" role="menu">
    <div class="SelectMenu-modal">
      <header class="SelectMenu-header">
        <span class="SelectMenu-title">Code definitions</span>
        <button class="SelectMenu-closeButton" type="button" data-toggle-for="jumpto-symbol-select-menu">
          <svg aria-label="Close menu" class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" role="img"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"></path></svg>
        </button>
      </header>
        <div class="SelectMenu-filter">
          <input
            class="SelectMenu-input form-control js-filterable-field"
            id="jumpto-symbols-filter-field"
            type="text"
            autocomplete="off"
            spellcheck="false"
            autofocus
            placeholder="Filter definitions"
            aria-label="Filter definitions">
        </div>
      <div class="SelectMenu-list">
        <div data-filterable-for="jumpto-symbols-filter-field" data-filterable-type="substring">
          <a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L7">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>NodeTest</span>
  <span class="flex-auto d-flex flex-justify-end">Class</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L9">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>test_init</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L12">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L13">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L16">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>LinkedListTest</span>
  <span class="flex-auto d-flex flex-justify-end">Class</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L18">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>test_init</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L20">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L21">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L22">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L24">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>test_init_with_list</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L26">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L27">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L28">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L30">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>test_items</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L32">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L34">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L36">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L38">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L40">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>test_length</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L42">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L45">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L47">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L49">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L52">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L54">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L56">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L58">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>test_size</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L60">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L63">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L65">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L67">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L70">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L72">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L74">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L76">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>test_get_at_index</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L78">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L79">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L80">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L86">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>test_insert_at_index</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L89">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L90">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L91">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L93">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L94">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L95">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L97">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L98">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L99">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L101">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L102">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L103">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L109">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>test_append</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L112">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L113">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L114">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L116">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L117">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L118">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L120">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L121">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L122">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L124">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>test_prepend</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L127">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L128">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L129">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L131">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L132">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L133">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L135">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L136">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L137">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L139">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>test_find</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L141">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L142">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L143">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L144">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L146">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>test_replace</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L149">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L150">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L151">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L153">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L154">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L155">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L157">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L158">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L159">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L163">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>test_delete</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L166">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L167">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L168">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L170">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L171">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L172">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L174">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L175">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a><a class="SelectMenu-item d-flex flex-justify-between css-truncate" role="menuitemradio" aria-checked="false" rel="nofollow" data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.navigate_to_blob_definition&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;navigate_to_blob_definition&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}" data-hydro-click-hmac="2d8bed1e5a1daf76e67f984f66e522c93ca8c083fc2ede2956fea87404cdeb4b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py#L176">
  <svg class="octicon octicon-check SelectMenu-icon SelectMenu-icon--check" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5L12 5z"></path></svg>
  <span class="flex-auto css-truncate-target" data-menu-button-text>assert</span>
  <span class="flex-auto d-flex flex-justify-end">Function</span>
</a>
        </div>
      </div>
      <footer class="SelectMenu-footer">
        <div class="d-flex flex-justify-between">
          Code navigation index up-to-date
          <svg class="octicon octicon-primitive-dot text-green" viewBox="0 0 8 16" version="1.1" width="8" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 8c0-2.2 1.8-4 4-4s4 1.8 4 4-1.8 4-4 4-4-1.8-4-4z"></path></svg>
        </div>
      </footer>
    </div>
  </details-menu>
</details>

      </h2>

      <div class="BtnGroup flex-shrink-0 d-none d-md-inline-block">
        <a href="/Make-School-Courses/CS-1.3-Core-Data-Structures/find/master"
              class="js-pjax-capture-input btn btn-sm BtnGroup-item"
              data-pjax
              data-hotkey="t">
          Find file
        </a>
        <clipboard-copy value="Code/linked-list/linkedlist_test.py" class="btn btn-sm BtnGroup-item">
          Copy path
        </clipboard-copy>
      </div>
    </div>



    <include-fragment src="/Make-School-Courses/CS-1.3-Core-Data-Structures/contributors/master/Code/linked-list/linkedlist_test.py" class="Box Box--condensed commit-loader">
      <div class="Box-body bg-blue-light f6">
        Fetching contributors&hellip;
      </div>

      <div class="Box-body d-flex flex-items-center" >
        <img alt="" class="loader-loading mr-2" src="https://github.githubassets.com/images/spinners/octocat-spinner-32-EAF2F5.gif" width="16" height="16" />
        <span class="text-red h6 loader-error">Cannot retrieve contributors at this time</span>
      </div>
</include-fragment>





    <div class="Box mt-3 position-relative
      ">
      
<div class="Box-header py-2 d-flex flex-column flex-shrink-0 flex-md-row flex-md-items-center">
  <div class="text-mono f6 flex-auto pr-3 flex-order-2 flex-md-order-1 mt-2 mt-md-0">

      182 lines (162 sloc)
      <span class="file-info-divider"></span>
    5.82 KB
  </div>

  <div class="d-flex py-1 py-md-0 flex-auto flex-order-1 flex-md-order-2 flex-sm-grow-0 flex-justify-between">

    <div class="BtnGroup">
      <a id="raw-url" class="btn btn-sm BtnGroup-item" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/raw/master/Code/linked-list/linkedlist_test.py">Raw</a>
        <a class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blame/master/Code/linked-list/linkedlist_test.py">Blame</a>
      <a rel="nofollow" class="btn btn-sm BtnGroup-item" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/commits/master/Code/linked-list/linkedlist_test.py">History</a>
    </div>


    <div>
          <a class="btn-octicon tooltipped tooltipped-nw js-remove-unless-platform"
             data-platforms="windows,mac"
             href="https://desktop.github.com"
             aria-label="Open this file in GitHub Desktop"
             data-ga-click="Repository, open with desktop">
              <svg class="octicon octicon-device-desktop" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M15 2H1c-.55 0-1 .45-1 1v9c0 .55.45 1 1 1h5.34c-.25.61-.86 1.39-2.34 2h8c-1.48-.61-2.09-1.39-2.34-2H15c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm0 9H1V3h14v8z"></path></svg>
          </a>

          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="inline-form js-update-url-with-hash" action="/Make-School-Courses/CS-1.3-Core-Data-Structures/edit/master/Code/linked-list/linkedlist_test.py" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="6SI2FTmX+UXVY2JgkOlN9ruWra79fiDLa5LCPiingGwGHTg/VM0yjVYxLEBOyYVzI8swWP1tV3slXWcjlGNQ7Q==" />
            <button class="btn-octicon tooltipped tooltipped-nw" type="submit"
              aria-label="Fork this project and edit the file" data-hotkey="e" data-disable-with>
              <svg class="octicon octicon-pencil" viewBox="0 0 14 16" version="1.1" width="14" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 011.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"></path></svg>
            </button>
</form>
          <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="inline-form" action="/Make-School-Courses/CS-1.3-Core-Data-Structures/delete/master/Code/linked-list/linkedlist_test.py" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="ECrxVz8UOKW+noc2QQe/qjLf5XLl4syakyKaGxcc0QPIiJgvVBNODbmclbvuWm2hFfIMScnNOswMIV01PdghWg==" />
            <button class="btn-octicon btn-octicon-danger tooltipped tooltipped-nw" type="submit"
              aria-label="Fork this project and delete the file" data-disable-with>
              <svg class="octicon octicon-trashcan" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"></path></svg>
            </button>
</form>    </div>
  </div>
</div>



      

  <div itemprop="text" class="Box-body p-0 blob-wrapper data type-python ">
      
<table class="highlight tab-size js-file-line-container" data-tab-size="8" data-paste-markdown-skip>
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class=pl-c>#!python</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line"><span class=pl-k>from</span> <span class=pl-s1>linkedlist</span> <span class=pl-k>import</span> <span class=pl-v>LinkedList</span>, <span class=pl-v>Node</span></td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class=pl-k>import</span> <span class=pl-s1>unittest</span></td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line"><span class=pl-k>class</span> <span class=pl-v>NodeTest</span>(<span class=pl-s1>unittest</span>.<span class=pl-v>TestCase</span>):</td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>test_init</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>data</span> <span class=pl-c1>=</span> <span class=pl-s>&#39;ABC&#39;</span></td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>node</span> <span class=pl-c1>=</span> <span class=pl-v>Node</span>(<span class=pl-s1>data</span>)</td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>node</span>.<span class=pl-s1>data</span> <span class=pl-c1>is</span> <span class=pl-s1>data</span></td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>node</span>.<span class=pl-s1>next</span> <span class=pl-c1>is</span> <span class=pl-c1>None</span></td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line"><span class=pl-k>class</span> <span class=pl-v>LinkedListTest</span>(<span class=pl-s1>unittest</span>.<span class=pl-v>TestCase</span>):</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>test_init</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span> <span class=pl-c1>=</span> <span class=pl-v>LinkedList</span>()</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>head</span> <span class=pl-c1>is</span> <span class=pl-c1>None</span></td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>tail</span> <span class=pl-c1>is</span> <span class=pl-c1>None</span></td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>size</span> <span class=pl-c1>==</span> <span class=pl-c1>0</span></td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>test_init_with_list</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span> <span class=pl-c1>=</span> <span class=pl-v>LinkedList</span>([<span class=pl-s>&#39;A&#39;</span>, <span class=pl-s>&#39;B&#39;</span>, <span class=pl-s>&#39;C&#39;</span>])</td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>head</span>.<span class=pl-s1>data</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;A&#39;</span>  <span class=pl-c># first item</span></td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>tail</span>.<span class=pl-s1>data</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;C&#39;</span>  <span class=pl-c># last item</span></td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>size</span> <span class=pl-c1>==</span> <span class=pl-c1>3</span></td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>test_items</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span> <span class=pl-c1>=</span> <span class=pl-v>LinkedList</span>()</td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-en>items</span>() <span class=pl-c1>==</span> []</td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span>.<span class=pl-en>append</span>(<span class=pl-s>&#39;B&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-en>items</span>() <span class=pl-c1>==</span> [<span class=pl-s>&#39;B&#39;</span>]</td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span>.<span class=pl-en>prepend</span>(<span class=pl-s>&#39;A&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-en>items</span>() <span class=pl-c1>==</span> [<span class=pl-s>&#39;A&#39;</span>, <span class=pl-s>&#39;B&#39;</span>]</td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span>.<span class=pl-en>append</span>(<span class=pl-s>&#39;C&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-en>items</span>() <span class=pl-c1>==</span> [<span class=pl-s>&#39;A&#39;</span>, <span class=pl-s>&#39;B&#39;</span>, <span class=pl-s>&#39;C&#39;</span>]</td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>test_length</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span> <span class=pl-c1>=</span> <span class=pl-v>LinkedList</span>()</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-en>length</span>() <span class=pl-c1>==</span> <span class=pl-c1>0</span></td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># append and prepend operations increase length</span></td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span>.<span class=pl-en>append</span>(<span class=pl-s>&#39;B&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-en>length</span>() <span class=pl-c1>==</span> <span class=pl-c1>1</span></td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span>.<span class=pl-en>prepend</span>(<span class=pl-s>&#39;A&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-en>length</span>() <span class=pl-c1>==</span> <span class=pl-c1>2</span></td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span>.<span class=pl-en>append</span>(<span class=pl-s>&#39;C&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-en>length</span>() <span class=pl-c1>==</span> <span class=pl-c1>3</span></td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># delete operations decrease length</span></td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span>.<span class=pl-en>delete</span>(<span class=pl-s>&#39;B&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-en>length</span>() <span class=pl-c1>==</span> <span class=pl-c1>2</span></td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span>.<span class=pl-en>delete</span>(<span class=pl-s>&#39;C&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-en>length</span>() <span class=pl-c1>==</span> <span class=pl-c1>1</span></td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span>.<span class=pl-en>delete</span>(<span class=pl-s>&#39;A&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-en>length</span>() <span class=pl-c1>==</span> <span class=pl-c1>0</span></td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>test_size</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span> <span class=pl-c1>=</span> <span class=pl-v>LinkedList</span>()</td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>size</span> <span class=pl-c1>==</span> <span class=pl-c1>0</span></td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># append and prepend operations increment size</span></td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span>.<span class=pl-en>append</span>(<span class=pl-s>&#39;B&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>size</span> <span class=pl-c1>==</span> <span class=pl-c1>1</span></td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span>.<span class=pl-en>prepend</span>(<span class=pl-s>&#39;A&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>size</span> <span class=pl-c1>==</span> <span class=pl-c1>2</span></td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span>.<span class=pl-en>append</span>(<span class=pl-s>&#39;C&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>size</span> <span class=pl-c1>==</span> <span class=pl-c1>3</span></td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line">        <span class=pl-c># delete operations decrement size</span></td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span>.<span class=pl-en>delete</span>(<span class=pl-s>&#39;B&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>size</span> <span class=pl-c1>==</span> <span class=pl-c1>2</span></td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span>.<span class=pl-en>delete</span>(<span class=pl-s>&#39;C&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>size</span> <span class=pl-c1>==</span> <span class=pl-c1>1</span></td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span>.<span class=pl-en>delete</span>(<span class=pl-s>&#39;A&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>size</span> <span class=pl-c1>==</span> <span class=pl-c1>0</span></td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>test_get_at_index</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span> <span class=pl-c1>=</span> <span class=pl-v>LinkedList</span>([<span class=pl-s>&#39;A&#39;</span>, <span class=pl-s>&#39;B&#39;</span>, <span class=pl-s>&#39;C&#39;</span>])</td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-en>get_at_index</span>(<span class=pl-c1>0</span>) <span class=pl-c1>==</span> <span class=pl-s>&#39;A&#39;</span>  <span class=pl-c># head item</span></td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-en>get_at_index</span>(<span class=pl-c1>1</span>) <span class=pl-c1>==</span> <span class=pl-s>&#39;B&#39;</span>  <span class=pl-c># middle item</span></td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-en>get_at_index</span>(<span class=pl-c1>2</span>) <span class=pl-c1>==</span> <span class=pl-s>&#39;C&#39;</span>  <span class=pl-c># tail item</span></td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>with</span> <span class=pl-s1>self</span>.<span class=pl-en>assertRaises</span>(<span class=pl-v>ValueError</span>):</td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>ll</span>.<span class=pl-en>get_at_index</span>(<span class=pl-c1>3</span>)  <span class=pl-c># index too high</span></td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>with</span> <span class=pl-s1>self</span>.<span class=pl-en>assertRaises</span>(<span class=pl-v>ValueError</span>):</td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>ll</span>.<span class=pl-en>get_at_index</span>(<span class=pl-c1>-</span><span class=pl-c1>1</span>)  <span class=pl-c># index too low</span></td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>test_insert_at_index</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span> <span class=pl-c1>=</span> <span class=pl-v>LinkedList</span>()</td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span>.<span class=pl-en>insert_at_index</span>(<span class=pl-c1>0</span>, <span class=pl-s>&#39;B&#39;</span>)  <span class=pl-c># append(&#39;B&#39;)</span></td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>head</span>.<span class=pl-s1>data</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;B&#39;</span>  <span class=pl-c># new head (at index 0)</span></td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>tail</span>.<span class=pl-s1>data</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;B&#39;</span>  <span class=pl-c># new tail (at index 0)</span></td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>size</span> <span class=pl-c1>==</span> <span class=pl-c1>1</span></td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span>.<span class=pl-en>insert_at_index</span>(<span class=pl-c1>0</span>, <span class=pl-s>&#39;A&#39;</span>)  <span class=pl-c># prepend(&#39;A&#39;)</span></td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>head</span>.<span class=pl-s1>data</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;A&#39;</span>  <span class=pl-c># new head (at index 0)</span></td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>tail</span>.<span class=pl-s1>data</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;B&#39;</span>  <span class=pl-c># unchanged (now at index 1)</span></td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>size</span> <span class=pl-c1>==</span> <span class=pl-c1>2</span></td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span>.<span class=pl-en>insert_at_index</span>(<span class=pl-c1>2</span>, <span class=pl-s>&#39;D&#39;</span>)  <span class=pl-c># append(&#39;D&#39;)</span></td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>head</span>.<span class=pl-s1>data</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;A&#39;</span>  <span class=pl-c># unchanged (at index 0)</span></td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>tail</span>.<span class=pl-s1>data</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;D&#39;</span>  <span class=pl-c># new tail (now at index 2)</span></td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>size</span> <span class=pl-c1>==</span> <span class=pl-c1>3</span></td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span>.<span class=pl-en>insert_at_index</span>(<span class=pl-c1>2</span>, <span class=pl-s>&#39;C&#39;</span>)  <span class=pl-c># insert &#39;C&#39; between &#39;B&#39; and &#39;D&#39;</span></td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>head</span>.<span class=pl-s1>data</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;A&#39;</span>  <span class=pl-c># unchanged (at index 0)</span></td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>tail</span>.<span class=pl-s1>data</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;D&#39;</span>  <span class=pl-c># unchanged (now at index 3)</span></td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>size</span> <span class=pl-c1>==</span> <span class=pl-c1>4</span></td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>with</span> <span class=pl-s1>self</span>.<span class=pl-en>assertRaises</span>(<span class=pl-v>ValueError</span>):</td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>ll</span>.<span class=pl-en>insert_at_index</span>(<span class=pl-c1>5</span>, <span class=pl-s>&#39;X&#39;</span>)  <span class=pl-c># index too high</span></td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>with</span> <span class=pl-s1>self</span>.<span class=pl-en>assertRaises</span>(<span class=pl-v>ValueError</span>):</td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>ll</span>.<span class=pl-en>insert_at_index</span>(<span class=pl-c1>-</span><span class=pl-c1>1</span>, <span class=pl-s>&#39;Y&#39;</span>)  <span class=pl-c># index too low</span></td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>test_append</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span> <span class=pl-c1>=</span> <span class=pl-v>LinkedList</span>()</td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span>.<span class=pl-en>append</span>(<span class=pl-s>&#39;A&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>head</span>.<span class=pl-s1>data</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;A&#39;</span>  <span class=pl-c># new head</span></td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>tail</span>.<span class=pl-s1>data</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;A&#39;</span>  <span class=pl-c># new tail</span></td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>size</span> <span class=pl-c1>==</span> <span class=pl-c1>1</span></td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span>.<span class=pl-en>append</span>(<span class=pl-s>&#39;B&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>head</span>.<span class=pl-s1>data</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;A&#39;</span>  <span class=pl-c># unchanged</span></td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>tail</span>.<span class=pl-s1>data</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;B&#39;</span>  <span class=pl-c># new tail</span></td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>size</span> <span class=pl-c1>==</span> <span class=pl-c1>2</span></td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span>.<span class=pl-en>append</span>(<span class=pl-s>&#39;C&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>head</span>.<span class=pl-s1>data</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;A&#39;</span>  <span class=pl-c># unchanged</span></td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>tail</span>.<span class=pl-s1>data</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;C&#39;</span>  <span class=pl-c># new tail</span></td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>size</span> <span class=pl-c1>==</span> <span class=pl-c1>3</span></td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>test_prepend</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span> <span class=pl-c1>=</span> <span class=pl-v>LinkedList</span>()</td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span>.<span class=pl-en>prepend</span>(<span class=pl-s>&#39;C&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>head</span>.<span class=pl-s1>data</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;C&#39;</span>  <span class=pl-c># new head</span></td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>tail</span>.<span class=pl-s1>data</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;C&#39;</span>  <span class=pl-c># new head</span></td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>size</span> <span class=pl-c1>==</span> <span class=pl-c1>1</span></td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span>.<span class=pl-en>prepend</span>(<span class=pl-s>&#39;B&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>head</span>.<span class=pl-s1>data</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;B&#39;</span>  <span class=pl-c># new head</span></td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>tail</span>.<span class=pl-s1>data</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;C&#39;</span>  <span class=pl-c># unchanged</span></td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>size</span> <span class=pl-c1>==</span> <span class=pl-c1>2</span></td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span>.<span class=pl-en>prepend</span>(<span class=pl-s>&#39;A&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>head</span>.<span class=pl-s1>data</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;A&#39;</span>  <span class=pl-c># new head</span></td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>tail</span>.<span class=pl-s1>data</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;C&#39;</span>  <span class=pl-c># unchanged</span></td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>size</span> <span class=pl-c1>==</span> <span class=pl-c1>3</span></td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>test_find</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span> <span class=pl-c1>=</span> <span class=pl-v>LinkedList</span>([<span class=pl-s>&#39;A&#39;</span>, <span class=pl-s>&#39;B&#39;</span>, <span class=pl-s>&#39;C&#39;</span>])</td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-en>find</span>(<span class=pl-k>lambda</span> <span class=pl-s1>item</span>: <span class=pl-s1>item</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;B&#39;</span>) <span class=pl-c1>==</span> <span class=pl-s>&#39;B&#39;</span></td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-en>find</span>(<span class=pl-k>lambda</span> <span class=pl-s1>item</span>: <span class=pl-s1>item</span> <span class=pl-c1>&lt;</span> <span class=pl-s>&#39;B&#39;</span>) <span class=pl-c1>==</span> <span class=pl-s>&#39;A&#39;</span></td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-en>find</span>(<span class=pl-k>lambda</span> <span class=pl-s1>item</span>: <span class=pl-s1>item</span> <span class=pl-c1>&gt;</span> <span class=pl-s>&#39;B&#39;</span>) <span class=pl-c1>==</span> <span class=pl-s>&#39;C&#39;</span></td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-en>find</span>(<span class=pl-k>lambda</span> <span class=pl-s1>item</span>: <span class=pl-s1>item</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;X&#39;</span>) <span class=pl-c1>is</span> <span class=pl-c1>None</span></td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>test_replace</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span> <span class=pl-c1>=</span> <span class=pl-v>LinkedList</span>([<span class=pl-s>&#39;A&#39;</span>, <span class=pl-s>&#39;B&#39;</span>, <span class=pl-s>&#39;C&#39;</span>])</td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span>.<span class=pl-en>replace</span>(<span class=pl-s>&#39;A&#39;</span>, <span class=pl-s>&#39;D&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>head</span>.<span class=pl-s1>data</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;D&#39;</span>  <span class=pl-c># new head</span></td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>tail</span>.<span class=pl-s1>data</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;C&#39;</span>  <span class=pl-c># unchanged</span></td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>size</span> <span class=pl-c1>==</span> <span class=pl-c1>3</span></td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span>.<span class=pl-en>replace</span>(<span class=pl-s>&#39;B&#39;</span>, <span class=pl-s>&#39;E&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>head</span>.<span class=pl-s1>data</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;D&#39;</span>  <span class=pl-c># unchanged</span></td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>tail</span>.<span class=pl-s1>data</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;C&#39;</span>  <span class=pl-c># unchanged</span></td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>size</span> <span class=pl-c1>==</span> <span class=pl-c1>3</span></td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span>.<span class=pl-en>replace</span>(<span class=pl-s>&#39;C&#39;</span>, <span class=pl-s>&#39;F&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>head</span>.<span class=pl-s1>data</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;D&#39;</span>  <span class=pl-c># unchanged</span></td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>tail</span>.<span class=pl-s1>data</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;F&#39;</span>  <span class=pl-c># new tail</span></td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>size</span> <span class=pl-c1>==</span> <span class=pl-c1>3</span></td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>with</span> <span class=pl-s1>self</span>.<span class=pl-en>assertRaises</span>(<span class=pl-v>ValueError</span>):</td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>ll</span>.<span class=pl-en>replace</span>(<span class=pl-s>&#39;X&#39;</span>, <span class=pl-s>&#39;Y&#39;</span>)  <span class=pl-c># item not in list</span></td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code blob-code-inner js-file-line">    <span class=pl-k>def</span> <span class=pl-en>test_delete</span>(<span class=pl-s1>self</span>):</td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span> <span class=pl-c1>=</span> <span class=pl-v>LinkedList</span>([<span class=pl-s>&#39;A&#39;</span>, <span class=pl-s>&#39;B&#39;</span>, <span class=pl-s>&#39;C&#39;</span>])</td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span>.<span class=pl-en>delete</span>(<span class=pl-s>&#39;A&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>head</span>.<span class=pl-s1>data</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;B&#39;</span>  <span class=pl-c># new head</span></td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>tail</span>.<span class=pl-s1>data</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;C&#39;</span>  <span class=pl-c># unchanged</span></td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>size</span> <span class=pl-c1>==</span> <span class=pl-c1>2</span></td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span>.<span class=pl-en>delete</span>(<span class=pl-s>&#39;C&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>head</span>.<span class=pl-s1>data</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;B&#39;</span>  <span class=pl-c># unchanged</span></td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>tail</span>.<span class=pl-s1>data</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;B&#39;</span>  <span class=pl-c># new tail</span></td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>size</span> <span class=pl-c1>==</span> <span class=pl-c1>1</span></td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code blob-code-inner js-file-line">        <span class=pl-s1>ll</span>.<span class=pl-en>delete</span>(<span class=pl-s>&#39;B&#39;</span>)</td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>head</span> <span class=pl-c1>is</span> <span class=pl-c1>None</span>  <span class=pl-c># new head</span></td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>tail</span> <span class=pl-c1>is</span> <span class=pl-c1>None</span>  <span class=pl-c># new head</span></td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>assert</span> <span class=pl-s1>ll</span>.<span class=pl-s1>size</span> <span class=pl-c1>==</span> <span class=pl-c1>0</span></td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code blob-code-inner js-file-line">        <span class=pl-k>with</span> <span class=pl-s1>self</span>.<span class=pl-en>assertRaises</span>(<span class=pl-v>ValueError</span>):</td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code blob-code-inner js-file-line">            <span class=pl-s1>ll</span>.<span class=pl-en>delete</span>(<span class=pl-s>&#39;X&#39;</span>)  <span class=pl-c># item not in list</span></td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code blob-code-inner js-file-line"><span class=pl-k>if</span> <span class=pl-s1>__name__</span> <span class=pl-c1>==</span> <span class=pl-s>&#39;__main__&#39;</span>:</td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code blob-code-inner js-file-line">    <span class=pl-s1>unittest</span>.<span class=pl-en>main</span>()</td>
      </tr>
</table>

  <details class="details-reset details-overlay BlobToolbar position-absolute js-file-line-actions dropdown d-none" aria-hidden="true">
    <summary class="btn-octicon ml-0 px-2 p-0 bg-white border border-gray-dark rounded-1" aria-label="Inline file action toolbar">
      <svg class="octicon octicon-kebab-horizontal" viewBox="0 0 13 16" version="1.1" width="13" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M1.5 9a1.5 1.5 0 100-3 1.5 1.5 0 000 3zm5 0a1.5 1.5 0 100-3 1.5 1.5 0 000 3zM13 7.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0z"></path></svg>
    </summary>
    <details-menu>
      <ul class="BlobToolbar-dropdown dropdown-menu dropdown-menu-se mt-2" style="width:185px">
        <li>
          <clipboard-copy role="menuitem" class="dropdown-item" id="js-copy-lines" style="cursor:pointer;">
            Copy lines
          </clipboard-copy>
        </li>
        <li>
          <clipboard-copy role="menuitem" class="dropdown-item" id="js-copy-permalink" style="cursor:pointer;">
            Copy permalink
          </clipboard-copy>
        </li>
        <li><a class="dropdown-item js-update-url-with-hash" id="js-view-git-blame" role="menuitem" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/blame/9c4c60e3227c913bb528f8cbb57fc3fb75561711/Code/linked-list/linkedlist_test.py">View git blame</a></li>
          <li><a class="dropdown-item" id="js-new-issue" role="menuitem" href="/Make-School-Courses/CS-1.3-Core-Data-Structures/issues/new">Reference in new issue</a></li>
      </ul>
    </details-menu>
  </details>

  </div>

    </div>

  

  <details class="details-reset details-overlay details-overlay-dark">
    <summary data-hotkey="l" aria-label="Jump to line"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast linejump" aria-label="Jump to line">
      <!-- '"` --><!-- </textarea></xmp> --></option></form><form class="js-jump-to-line-form Box-body d-flex" action="" accept-charset="UTF-8" method="get">
        <input class="form-control flex-auto mr-3 linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
        <button type="submit" class="btn" data-close-dialog>Go</button>
</form>    </details-dialog>
  </details>

    <div class="Popover anim-scale-in js-tagsearch-popover"
     hidden
     data-tagsearch-url="/Make-School-Courses/CS-1.3-Core-Data-Structures/find-symbols"
     data-tagsearch-ref="master"
     data-tagsearch-path="Code/linked-list/linkedlist_test.py"
     data-tagsearch-lang="Python"
     data-hydro-click="{&quot;event_type&quot;:&quot;code_navigation.click_on_symbol&quot;,&quot;payload&quot;:{&quot;action&quot;:&quot;click_on_symbol&quot;,&quot;repository_id&quot;:164776962,&quot;ref&quot;:&quot;master&quot;,&quot;language&quot;:&quot;Python&quot;,&quot;originating_url&quot;:&quot;https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Code/linked-list/linkedlist_test.py&quot;,&quot;user_id&quot;:10855238}}"
     data-hydro-click-hmac="1d918350fa3646cdc4ee1a14cddab28c673fe6f45788f38eedc69905eeea0294">
  <div class="Popover-message Popover-message--large Popover-message--top-left TagsearchPopover mt-1 mb-4 mx-auto Box box-shadow-large">
    <div class="TagsearchPopover-content js-tagsearch-popover-content overflow-auto" style="will-change:transform;">
    </div>
  </div>
</div>



  </div>
</div>

    </main>
  </div>
  

  </div>

        
<div class="footer container-lg width-full p-responsive" role="contentinfo">
  <div class="position-relative d-flex flex-row-reverse flex-lg-row flex-wrap flex-lg-nowrap flex-justify-center flex-lg-justify-between pt-6 pb-2 mt-6 f6 text-gray border-top border-gray-light ">
    <ul class="list-style-none d-flex flex-wrap col-12 col-lg-5 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
      <li class="mr-3 mr-lg-0">&copy; 2020 GitHub, Inc.</li>
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to terms, text:terms" href="https://github.com/site/terms">Terms</a></li>
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to privacy, text:privacy" href="https://github.com/site/privacy">Privacy</a></li>
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to security, text:security" href="https://github.com/security">Security</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://githubstatus.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a data-ga-click="Footer, go to help, text:help" href="https://help.github.com">Help</a></li>

    </ul>

    <a aria-label="Homepage" title="GitHub" class="footer-octicon d-none d-lg-block mx-lg-4" href="https://github.com">
      <svg height="24" class="octicon octicon-mark-github" viewBox="0 0 16 16" version="1.1" width="24" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>
</a>
   <ul class="list-style-none d-flex flex-wrap col-12 col-lg-5 flex-justify-center flex-lg-justify-between mb-2 mb-lg-0">
        <li class="mr-3 mr-lg-0"><a data-ga-click="Footer, go to contact, text:contact" href="https://github.com/contact">Contact GitHub</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://github.com/pricing" data-ga-click="Footer, go to Pricing, text:Pricing">Pricing</a></li>
      <li class="mr-3 mr-lg-0"><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3 mr-lg-0"><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
        <li class="mr-3 mr-lg-0"><a href="https://github.blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a data-ga-click="Footer, go to about, text:about" href="https://github.com/about">About</a></li>
    </ul>
  </div>
  <div class="d-flex flex-justify-center pb-6">
    <span class="f6 text-gray-light"></span>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 000 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 00.01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"></path></svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"></path></svg>
    </button>
    You can’t perform that action at this time.
  </div>


    <script crossorigin="anonymous" async="async" integrity="sha512-WcQmT2vhcClFVOaaAJV/M+HqsJ2Gq/myvl6F3gCVBxykazXTs+i5fvxncSXwyG1CSfcrqmLFw/R/bmFYzprX2A==" type="application/javascript" id="js-conditional-compat" data-src="https://github.githubassets.com/assets/compat-bootstrap-59c4264f.js"></script>
    <script crossorigin="anonymous" integrity="sha512-LVxS1PfjfeHqYi4XeQewJV46GKFXUJ6h4NWxgEeuqVFKQYc3n/hs6ZjCBUj7cEJqgkhz/nQ1L/nRSCOTNCgLng==" type="application/javascript" src="https://github.githubassets.com/assets/environment-bootstrap-2d5c52d4.js"></script>
      <script crossorigin="anonymous" async="async" integrity="sha512-327XCyOytNBlvvFRes7NYmY/gSME67CreRw+pR2DhNKBfEb2Sv0pe/XkZUSqYYlgGdDnaGIKUAb4oRZBLdKBfw==" type="application/javascript" src="https://github.githubassets.com/assets/vendor-df6ed70b.js"></script>
      <script crossorigin="anonymous" async="async" integrity="sha512-wnxLD0FLGLvL6Z6J0ONtO21sujNdLja3rEt6olICYjPDmBnvVCwib2UplrQNnxAu5U2dMElP/8aGWEI4wNSFJw==" type="application/javascript" src="https://github.githubassets.com/assets/frameworks-c27c4b0f.js"></script>
    
    <script crossorigin="anonymous" async="async" integrity="sha512-NWHSS/nmSHSsXKmQvpGMETf9+vBnrv/nX+ZlPAhJi5ThleYvSCMMDpsZx2cvOeXrM0Ih4zs3mtoKbxsvC+DvNg==" type="application/javascript" src="https://github.githubassets.com/assets/github-bootstrap-3561d24b.js"></script>
    
    
    
  <div class="js-stale-session-flash flash flash-warn flash-banner" hidden
    >
    <svg class="octicon octicon-alert" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M8.893 1.5c-.183-.31-.52-.5-.887-.5s-.703.19-.886.5L.138 13.499a.98.98 0 000 1.001c.193.31.53.501.886.501h13.964c.367 0 .704-.19.877-.5a1.03 1.03 0 00.01-1.002L8.893 1.5zm.133 11.497H6.987v-2.003h2.039v2.003zm0-3.004H6.987V5.987h2.039v4.006z"></path></svg>
    <span class="js-stale-session-flash-signed-in" hidden>You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="js-stale-session-flash-signed-out" hidden>You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <template id="site-details-dialog">
  <details class="details-reset details-overlay details-overlay-dark lh-default text-gray-dark hx_rsm" open>
    <summary role="button" aria-label="Close dialog"></summary>
    <details-dialog class="Box Box--overlay d-flex flex-column anim-fade-in fast hx_rsm-dialog hx_rsm-modal">
      <button class="Box-btn-octicon m-0 btn-octicon position-absolute right-0 top-0" type="button" aria-label="Close dialog" data-close-dialog>
        <svg class="octicon octicon-x" viewBox="0 0 12 16" version="1.1" width="12" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48L7.48 8z"></path></svg>
      </button>
      <div class="octocat-spinner my-6 js-details-dialog-spinner"></div>
    </details-dialog>
  </details>
</template>

  <div class="Popover js-hovercard-content position-absolute" style="display: none; outline: none;" tabindex="0">
  <div class="Popover-message Popover-message--bottom-left Popover-message--large Box box-shadow-large" style="width:360px;">
  </div>
</div>


  </body>
</html>
