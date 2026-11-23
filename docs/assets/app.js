// Remembers the chosen context and profile, then shows only the matching blocks.
// Choice sources, by priority: URL parameters (?ctx=…&profile=…), then localStorage.
// Displayed labels are French (site language).
(function () {
  var CHOICES = {
    ctx: { cabinet: "Cabinet libéral", labo: "Laboratoire de biologie", hopital: "Hôpital public" },
    profile: { employe: "Employé (accueil, secrétariat)", it: "Équipe IT", dirigeant: "Dirigeant" }
  };

  function readStorage(key) {
    try { return localStorage.getItem("practilio-" + key); } catch (e) { return null; }
  }
  function writeStorage(key, value) {
    try { localStorage.setItem("practilio-" + key, value); } catch (e) { /* storage unavailable */ }
  }

  var params = new URLSearchParams(location.search);
  var state = {};
  Object.keys(CHOICES).forEach(function (key) {
    var value = params.get(key) || readStorage(key);
    state[key] = CHOICES[key][value] ? value : null;
    if (state[key]) writeStorage(key, state[key]);
  });

  // Answers to the complementary questions, remembered per question ("1" = ticked)
  var answers = {};
  var questions = document.querySelector(".questions");
  if (questions) {
    questions.querySelectorAll("input[data-question]").forEach(function (box) {
      var key = box.getAttribute("data-question");
      answers[key] = readStorage("q-" + key) === "1";
      box.checked = answers[key];
      box.addEventListener("change", function () {
        answers[key] = box.checked;
        writeStorage("q-" + key, box.checked ? "1" : "0");
        apply();
      });
    });
    questions.hidden = false;
  }

  function apply() {
    Object.keys(CHOICES).forEach(function (key) {
      // Context- or profile-specific blocks: hidden when another value is chosen
      document.querySelectorAll("[data-" + key + "]").forEach(function (el) {
        var values = el.getAttribute("data-" + key).split(" ");
        el.hidden = !!state[key] && values.indexOf(state[key]) === -1;
      });
      // "Please choose first" hints
      document.querySelectorAll("[data-no-" + key + "]").forEach(function (el) {
        el.hidden = !!state[key];
      });
      // Selector buttons
      document.querySelectorAll("button[data-pick-" + key + "]").forEach(function (button) {
        button.setAttribute("aria-pressed", String(button.getAttribute("data-pick-" + key) === state[key]));
      });
    });

    // Complementary questions (obligations.html): "key" shows when ticked, "!key" when not
    document.querySelectorAll("[data-if]").forEach(function (el) {
      var cond = el.getAttribute("data-if");
      var negate = cond.charAt(0) === "!";
      el.hidden = answers[negate ? cond.slice(1) : cond] === negate;
    });

    syncMatrix();
    syncTabs();

    // Reminder of the current choice in the header
    var reminder = document.getElementById("current-choice");
    if (reminder) {
      var ctx = state.ctx ? CHOICES.ctx[state.ctx] : "contexte non choisi";
      var profile = state.profile ? CHOICES.profile[state.profile] : "profil non choisi";
      reminder.textContent = "Votre parcours : " + ctx + " · " + profile + " · ";
      var link = document.createElement("a");
      link.href = "index.html#je-suis";
      link.textContent = "changer";
      reminder.appendChild(link);
    }

    // Internal links carry the choice (useful when storage is blocked)
    var query = new URLSearchParams();
    Object.keys(state).forEach(function (key) { if (state[key]) query.set(key, state[key]); });
    document.querySelectorAll("a[href$='.html'], a[href*='.html?'], a[href*='.html#']").forEach(function (a) {
      var href = a.getAttribute("href");
      if (/^https?:/.test(href)) return;
      var parts = href.split("#");
      var base = parts[0].split("?")[0];
      a.setAttribute("href", base + (query.toString() ? "?" + query.toString() : "") + (parts[1] ? "#" + parts[1] : ""));
    });
  }

  // ---- In-page tabs (risques.html, premiers-pas.html, ressources.html) ----
  // Without JavaScript the tab bar is a list of in-page links and every panel is shown.
  // A link or URL hash pointing inside a panel opens that panel.
  var tabSets = Array.prototype.slice.call(document.querySelectorAll("[data-tabs]"));

  function selectTab(set, id, focus) {
    set.querySelectorAll(".tab-list a").forEach(function (tab) {
      var on = tab.getAttribute("data-tab") === id;
      tab.setAttribute("aria-selected", String(on));
      tab.tabIndex = on ? 0 : -1;
      if (on && focus) tab.focus();
    });
    set.querySelectorAll(".tab-panel").forEach(function (panel) {
      panel.hidden = panel.id !== id;
    });
  }

  // A panel is empty when none of its context / profile sections has visible content
  // (obligations.html: a text that does not apply to the chosen context or answers)
  function panelHasContent(panel) {
    var sections = panel.querySelectorAll("section[data-ctx], section[data-profile]");
    if (!sections.length) return true;
    return Array.prototype.some.call(sections, function (section) {
      if (section.hidden) return false;
      var blocks = section.querySelectorAll(".block");
      if (!blocks.length) return true;  // "À remplir" box
      return Array.prototype.some.call(blocks, function (block) {
        return Array.prototype.some.call(block.children, function (child) { return !child.hidden; });
      });
    });
  }

  // Hides the tabs with an empty panel; if the open tab is hidden, opens the first visible one
  function syncTabs() {
    tabSets.forEach(function (set) {
      var tabs = Array.prototype.slice.call(set.querySelectorAll(".tab-list a[data-tab]"));
      var current = null;
      tabs.forEach(function (tab) {
        tab.hidden = !panelHasContent(document.getElementById(tab.getAttribute("data-tab")));
        if (!tab.hidden && tab.getAttribute("aria-selected") === "true") current = tab;
      });
      var first = tabs.filter(function (tab) { return !tab.hidden; })[0];
      if (!current && first) selectTab(set, first.getAttribute("data-tab"), false);
    });
  }

  // Opens the tab holding el; returns true if el sits in a tab panel
  function revealTab(el) {
    var panel = el && el.closest && el.closest(".tab-panel");
    if (!panel) return false;
    var set = panel.closest("[data-tabs]");
    if (set && panel.hidden) selectTab(set, panel.id, false);
    return true;
  }

  function targetOf(hash) {
    if (!hash || hash.length < 2) return null;
    try { return document.getElementById(decodeURIComponent(hash.slice(1))); } catch (e) { return null; }
  }

  if (tabSets.length) document.documentElement.classList.add("js-tabs");
  tabSets.forEach(function (set) {
    var list = set.querySelector(".tab-list");
    var tabs = Array.prototype.slice.call(list.querySelectorAll("a[data-tab]"));
    list.setAttribute("role", "tablist");
    tabs.forEach(function (tab) {
      var id = tab.getAttribute("data-tab");
      tab.setAttribute("role", "tab");
      tab.id = "tab-" + id;
      tab.setAttribute("aria-controls", id);
      var panel = document.getElementById(id);
      panel.setAttribute("role", "tabpanel");
      panel.setAttribute("aria-labelledby", tab.id);
      tab.addEventListener("click", function (event) {
        event.preventDefault();
        selectTab(set, id, false);
        history.replaceState(null, "", location.pathname + location.search + "#" + id);
      });
      tab.addEventListener("keydown", function (event) {
        var visible = tabs.filter(function (t) { return !t.hidden; });
        var i = visible.indexOf(tab);
        var to = event.key === "ArrowRight" ? i + 1 : event.key === "ArrowLeft" ? i - 1
          : event.key === "Home" ? 0 : event.key === "End" ? visible.length - 1 : null;
        if (to === null) return;
        event.preventDefault();
        to = (to + visible.length) % visible.length;
        selectTab(set, visible[to].getAttribute("data-tab"), true);
      });
    });
    // First tab by default, unless the URL points inside another panel
    var target = targetOf(location.hash);
    var start = target && target.closest(".tab-panel");
    selectTab(set, start && set.contains(start) ? start.id : tabs[0].getAttribute("data-tab"), false);
    if (start && set.contains(start)) target.scrollIntoView();
  });

  if (tabSets.length) {
    window.addEventListener("hashchange", function () {
      var target = targetOf(location.hash);
      if (revealTab(target)) target.scrollIntoView();
    });
    // A click on a link to the current hash fires no hashchange: handle in-page links directly
    document.addEventListener("click", function (event) {
      var a = event.target.closest("a[href^='#']");
      if (!a || a.hasAttribute("data-tab")) return;
      var target = targetOf(a.getAttribute("href"));
      if (target && target.closest(".tab-panel") && target.closest(".tab-panel").hidden) {
        revealTab(target);
        if (location.hash === a.getAttribute("href")) target.scrollIntoView();
      }
    });
  }

  // ---- Threat matrix (risques.html): a click on a cell shows its card in the panel ----
  var matrix = document.querySelector(".matrix");
  var panel = document.getElementById("threat-panel");
  var compareButton = document.querySelector("[data-matrix-compare]");
  var activeCell = null;

  function syncMatrix() {
    if (!matrix) return;
    matrix.classList.toggle("has-current", !!state.ctx);
    matrix.querySelectorAll("[data-col]").forEach(function (cell) {
      cell.classList.toggle("current", cell.getAttribute("data-col") === state.ctx);
    });
    if (compareButton) compareButton.hidden = !state.ctx;
  }

  function openThreat(id, focus) {
    var card = id && document.getElementById(id);
    if (!panel || !card || !card.classList.contains("threat")) return false;
    var body = panel.querySelector(".threat-panel-body");
    var title = document.getElementById("threat-panel-title");
    title.innerHTML = "";
    title.appendChild(card.querySelector("summary .level").cloneNode(true));
    var other = card.id.indexOf("menace-" + state.ctx + "-") !== 0;
    title.appendChild(document.createTextNode(" " + card.getAttribute("data-title") +
      (other ? " · " + card.getAttribute("data-ctx-label") : "")));
    body.innerHTML = card.querySelector(".block").innerHTML;
    revealTab(panel);
    panel.hidden = false;
    if (activeCell) activeCell.removeAttribute("aria-current");
    activeCell = matrix.querySelector('a[href="#' + id + '"]');
    if (activeCell) activeCell.setAttribute("aria-current", "true");
    if (focus) title.focus();
    return true;
  }

  function closeThreat() {
    if (!panel || panel.hidden) return;
    panel.hidden = true;
    history.replaceState(null, "", location.pathname + location.search);
    if (activeCell) { activeCell.removeAttribute("aria-current"); activeCell.focus(); }
  }

  if (matrix && panel) {
    document.documentElement.classList.add("js-matrix");  // hides the plain card list (CSS)
    matrix.addEventListener("click", function (event) {
      var cell = event.target.closest("a.cell");
      if (!cell) return;
      event.preventDefault();
      var id = cell.getAttribute("href").slice(1);
      if (openThreat(id, true)) history.replaceState(null, "", location.pathname + location.search + "#" + id);
    });
    panel.querySelector(".threat-panel-close").addEventListener("click", closeThreat);
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") closeThreat();
    });
    if (compareButton) compareButton.addEventListener("click", function () {
      var on = !matrix.classList.contains("compare");
      matrix.classList.toggle("compare", on);
      compareButton.setAttribute("aria-pressed", String(on));
    });
    // Deep link, e.g. risques.html#menace-hopital-ot
    if (openThreat(location.hash.slice(1), false)) panel.scrollIntoView();
    // In-page links to a threat (e.g. from the "Ça s'est vraiment passé" cards)
    window.addEventListener("hashchange", function () {
      if (openThreat(location.hash.slice(1), false)) panel.scrollIntoView();
    });
  }

  document.addEventListener("click", function (event) {
    var button = event.target.closest("button");
    if (!button) return;
    Object.keys(CHOICES).forEach(function (key) {
      var value = button.getAttribute("data-pick-" + key);
      if (value && CHOICES[key][value]) {
        state[key] = value;
        writeStorage(key, value);
        var p = new URLSearchParams(location.search);
        p.set(key, value);
        history.replaceState(null, "", location.pathname + "?" + p.toString() + location.hash);
        apply();
      }
    });
  });

  // "Ça s'est vraiment passé": one attack card at a time, with previous/next buttons and dots.
  // Without JavaScript the cards stay stacked (the CSS only applies under .js-carousel).
  var carousels = document.querySelectorAll(".carousel");
  if (carousels.length) document.documentElement.classList.add("js-carousel");
  Array.prototype.forEach.call(carousels, function (carousel) {
    var track = carousel.querySelector(".carousel-track");
    var slides = Array.prototype.slice.call(track.querySelectorAll(".attack"));
    var nav = carousel.querySelector(".carousel-nav");
    if (slides.length < 2) return;
    var prev = nav.querySelector(".carousel-prev");
    var next = nav.querySelector(".carousel-next");
    var count = nav.querySelector(".carousel-count");
    var dots = document.createElement("span");
    dots.className = "carousel-dots";
    slides.forEach(function (slide, n) {
      var dot = document.createElement("button");
      dot.type = "button";
      dot.setAttribute("aria-label", "Fiche " + (n + 1) + " : " + slide.querySelector("h4").textContent);
      dot.addEventListener("click", function () { go(n); });
      dots.appendChild(dot);
    });
    nav.insertBefore(dots, next);
    var current = -1;

    function mark(n) {
      if (n === current) return;
      current = n;
      count.textContent = (n + 1) + " / " + slides.length;
      prev.disabled = n === 0;
      next.disabled = n === slides.length - 1;
      Array.prototype.forEach.call(dots.children, function (dot, i) {
        dot.setAttribute("aria-current", String(i === n));
      });
    }
    function go(n) {
      n = Math.max(0, Math.min(slides.length - 1, n));
      track.scrollTo({ left: slides[n].offsetLeft });
      mark(n);
    }
    prev.addEventListener("click", function () { go(current - 1); });
    next.addEventListener("click", function () { go(current + 1); });
    track.addEventListener("keydown", function (event) {
      if (event.target !== track) return;
      if (event.key === "ArrowLeft") { event.preventDefault(); go(current - 1); }
      if (event.key === "ArrowRight") { event.preventDefault(); go(current + 1); }
    });
    // Swipe or trackpad scroll: follow the card closest to the left edge
    var timer;
    track.addEventListener("scroll", function () {
      clearTimeout(timer);
      timer = setTimeout(function () {
        var best = 0;
        slides.forEach(function (slide, i) {
          if (Math.abs(slide.offsetLeft - track.scrollLeft) < Math.abs(slides[best].offsetLeft - track.scrollLeft)) best = i;
        });
        mark(best);
      }, 80);
    });
    mark(0);
    nav.hidden = false;
  });

  // ---- Quizzes (evaluer.html): score, correction, last result kept in this browser only ----
  document.querySelectorAll("form.quiz").forEach(function (form) {
    var key = "quiz-" + form.getAttribute("data-quiz");
    var actions = form.querySelector(".quiz-actions");
    var score = form.querySelector(".quiz-score");
    var last = form.querySelector(".quiz-last");
    function showLast() {
      var saved = readStorage(key);
      if (saved) { last.textContent = "Votre dernier résultat : " + saved; last.hidden = false; }
    }
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      var questions = form.querySelectorAll(".quiz-q");
      var good = 0;
      questions.forEach(function (q) {
        var picked = q.querySelector("input:checked");
        q.classList.remove("is-right", "is-wrong");
        if (picked) q.classList.add(picked.hasAttribute("data-correct") ? "is-right" : "is-wrong");
        if (picked && picked.hasAttribute("data-correct")) good++;
        q.querySelector(".quiz-answer").open = true;
      });
      var result = good + " / " + questions.length;
      score.textContent = "Score : " + result;
      writeStorage(key, result + " (" + new Date().toLocaleDateString("fr-FR") + ")");
      showLast();
    });
    actions.hidden = false;
    showLast();
  });

  apply();
})();
