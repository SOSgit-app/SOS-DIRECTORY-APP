"""Convert Flask Jinja templates into static HTML for GitHub Pages."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def convert_static_urls(html: str) -> str:
    html = re.sub(
        r"\{\{\s*url_for\('static',\s*filename='([^']+)'\)\s*\}\}",
        r"static/\1",
        html,
    )
    html = html.replace("{{ url_for('dha_remote_access') }}", "dha-remote-access.html")
    html = html.replace("{{ url_for('index') }}", "index.html")
    return html


OLD_SEARCH = r"""        const searchInput = document.getElementById('searchInput');
        const resultsDiv = document.getElementById('results');
        let debounceTimeout;

        searchInput.addEventListener('input', function() {
            clearTimeout(debounceTimeout);
            debounceTimeout = setTimeout(() => {
                const query = this.value.trim();
                if (query.length < 2) {
                    resultsDiv.innerHTML = '';
                    return;
                }
                
                fetch(`/search?query=${encodeURIComponent(query)}`)
                    .then(response => response.json())
                    .then(data => {
                        if (data.length === 0) {
                            resultsDiv.innerHTML = '<div class="no-results">No students found</div>';
                            return;
                        }

                        resultsDiv.innerHTML = data.map(student => `
                            <div class="result-card">
                                <div class="student-name">${student.student_name}</div>
                                <div class="flight-info">Flight: ${student.flight_number}</div>
                                <div class="instructor-info">Instructor: ${student.instructor_name}</div>
                            </div>
                        `).join('');
                    })
                    .catch(error => {
                        console.error('Error:', error);
                        resultsDiv.innerHTML = '<div class="no-results">An error occurred while searching</div>';
                    });
            }, 300);
        });"""

NEW_SEARCH = r"""        const searchInput = document.getElementById('searchInput');
        const resultsDiv = document.getElementById('results');
        let debounceTimeout;
        let rosterData = null;
        let rosterLoadPromise = null;

        function loadRoster() {
            if (rosterData) return Promise.resolve(rosterData);
            if (rosterLoadPromise) return rosterLoadPromise;
            rosterLoadPromise = fetch('static/roster_data.json')
                .then(response => {
                    if (!response.ok) throw new Error('Failed to load roster');
                    return response.json();
                })
                .then(data => {
                    rosterData = data;
                    return rosterData;
                })
                .catch(error => {
                    rosterLoadPromise = null;
                    throw error;
                });
            return rosterLoadPromise;
        }

        // Prefetch roster for snappy search
        loadRoster().catch(err => console.error('Roster preload failed:', err));

        searchInput.addEventListener('input', function() {
            clearTimeout(debounceTimeout);
            debounceTimeout = setTimeout(() => {
                const query = this.value.trim();
                if (query.length < 2) {
                    resultsDiv.innerHTML = '';
                    return;
                }

                const searchTerm = query.toUpperCase();
                loadRoster()
                    .then(students => {
                        const data = students.filter(student =>
                            (student.student_name || '').toUpperCase().includes(searchTerm)
                        );

                        if (data.length === 0) {
                            resultsDiv.innerHTML = '<div class="no-results">No students found</div>';
                            return;
                        }

                        resultsDiv.innerHTML = data.map(student => `
                            <div class="result-card">
                                <div class="student-name">${student.student_name}</div>
                                <div class="flight-info">Flight: ${student.flight_number}</div>
                                <div class="instructor-info">Instructor: ${student.instructor_name}</div>
                            </div>
                        `).join('');
                    })
                    .catch(error => {
                        console.error('Error:', error);
                        resultsDiv.innerHTML = '<div class="no-results">An error occurred while searching</div>';
                    });
            }, 300);
        });"""


def build_index() -> None:
    index = (ROOT / "templates" / "index.html").read_text(encoding="utf-8")
    index = convert_static_urls(index)
    if OLD_SEARCH not in index:
        raise SystemExit("Old search block not found in templates/index.html")
    index = index.replace(OLD_SEARCH, NEW_SEARCH)
    (ROOT / "index.html").write_text(index, encoding="utf-8")
    print("Wrote index.html")


def build_dha() -> None:
    dha = (ROOT / "templates" / "dha_remote_access.html").read_text(encoding="utf-8")
    loop = """                {% for n in [1, 2, 3, 4] %}
                <div class="step-container">
                    <div class="step-label">Step {{ n }}</div>
                    <img src="{{ url_for('static', filename='DHA/Slide' ~ n ~ '.PNG') }}"
                         alt="DHA Remote Access step {{ n }}"
                         class="dha-slide">
                </div>
                {% endfor %}"""
    expanded = "".join(
        f"""                <div class="step-container">
                    <div class="step-label">Step {n}</div>
                    <img src="static/DHA/Slide{n}.PNG"
                         alt="DHA Remote Access step {n}"
                         class="dha-slide">
                </div>
"""
        for n in [1, 2, 3, 4]
    )
    if loop not in dha:
        raise SystemExit("DHA loop not found")
    dha = dha.replace(loop, expanded)
    dha = convert_static_urls(dha)
    (ROOT / "dha-remote-access.html").write_text(dha, encoding="utf-8")
    print("Wrote dha-remote-access.html")


if __name__ == "__main__":
    build_index()
    build_dha()
    print("Static site build complete")
