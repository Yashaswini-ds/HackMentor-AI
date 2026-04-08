document.addEventListener('DOMContentLoaded', () => {
    
    // --- Navigation Logic ---
    const navItems = document.querySelectorAll('.nav-item');
    const sections = document.querySelectorAll('.section');

    navItems.forEach(item => {
        item.addEventListener('click', () => {
            // Update active nav
            navItems.forEach(nav => nav.classList.remove('active'));
            item.classList.add('active');

            // Show target section
            const targetId = item.getAttribute('data-target');
            sections.forEach(sec => {
                if(sec.id === targetId) {
                    sec.classList.remove('hidden');
                } else {
                    sec.classList.add('hidden');
                }
            });
        });
    });

    // --- Loading UI ---
    const loading = document.getElementById('loadingOverlay');
    const showLoading = () => loading.style.display = 'block';
    const hideLoading = () => loading.style.display = 'none';

    // --- Helper to Pre-fill Data across tabs ---
    function useIdea(ideaText) {
        document.getElementById('ideaToScore').value = ideaText;
        document.getElementById('ideaToBuild').value = ideaText;
        document.getElementById('ideaToPitch').value = ideaText;
        
        // Switch to Scoring Tab
        document.querySelector('[data-target="scoring"]').click();
        
        // Auto-scroll to top
        window.scrollTo(0,0);
    }

    // --- 1. Idea Generation ---
    document.getElementById('ideaForm').addEventListener('submit', async (e) => {
        e.preventDefault();
        showLoading();
        
        const payload = {
            domain: document.getElementById('domain').value,
            problem: document.getElementById('problem').value,
            tech_level: document.getElementById('techLevel').value
        };

        try {
            const res = await fetch('/api/generate-ideas', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(payload)
            });
            const data = await res.json();
            
            const container = document.getElementById('ideasContainer');
            container.innerHTML = '';
            
            if(data.ideas && data.ideas.length > 0) {
                data.ideas.forEach(idea => {
                    const card = document.createElement('div');
                    card.className = 'idea-card';
                    card.innerHTML = `
                        <h3 class="idea-title">${idea.title}</h3>
                        <p class="tagline">"${idea.tagline}"</p>
                        <p style="color:var(--text-muted); margin-bottom:1rem;"><strong>Problem:</strong> ${idea.problem_solved}</p>
                        <div>
                            <strong>Core Features:</strong>
                            <ul style="margin-left: 1.5rem; color:var(--text-muted); font-size:0.9rem;">
                                ${idea.core_features.map(f => `<li>${f}</li>`).join('')}
                            </ul>
                        </div>
                        <button class="use-idea-btn" style="margin-top:1rem; padding: 0.5rem; font-size: 0.9rem;">Analyze this Idea →</button>
                    `;
                    
                    const btn = card.querySelector('.use-idea-btn');
                    btn.onclick = () => {
                        const fullIdea = `${idea.title}: ${idea.tagline}. Problem: ${idea.problem_solved}. Features: ${idea.core_features.join(', ')}`;
                        document.getElementById('scoreDomain').value = payload.domain;
                        useIdea(fullIdea);
                    };
                    
                    container.appendChild(card);
                });
                document.getElementById('ideasResult').classList.remove('hidden');
            } else {
                container.innerHTML = `<p style="color:var(--danger)">Error: ${data.error || 'Failed to generate ideas.'}</p>`;
            }
        } catch (err) {
            console.error(err);
        } finally {
            hideLoading();
        }
    });

    // --- 2. Hybrid Scoring ---
    document.getElementById('scoreForm').addEventListener('submit', async (e) => {
        e.preventDefault();
        showLoading();
        
        const payload = {
            idea: document.getElementById('ideaToScore').value,
            domain: document.getElementById('scoreDomain').value,
            team_size: document.getElementById('teamSize').value,
            timeline_hours: document.getElementById('timeline').value,
            tech_level: document.getElementById('techLevel').value // pulling from tab 1
        };

        try {
            const res = await fetch('/api/score-idea', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(payload)
            });
            const data = await res.json();
            
            if(data.error) {
                alert("Error: " + data.error);
                hideLoading();
                return;
            }

            // Populate UI
            document.getElementById('verdictText').innerText = data.verdict;
            document.getElementById('totalScoreText').innerText = data.total_score;
            
            document.getElementById('scoreInnovation').innerText = data.final_scores.innovation;
            document.getElementById('reasonInnovation').innerText = data.initial_llm_scores.innovation.reasoning;
            
            document.getElementById('scoreFeasibility').innerText = data.final_scores.feasibility;
            document.getElementById('reasonFeasibility').innerText = data.initial_llm_scores.feasibility.reasoning;
            
            document.getElementById('scoreImpact').innerText = data.final_scores.impact;
            document.getElementById('reasonImpact').innerText = data.initial_llm_scores.impact.reasoning;

            // Adjustments
            const adjContainer = document.getElementById('adjustmentsContainer');
            const adjList = document.getElementById('adjustmentsList');
            adjList.innerHTML = '';
            
            if(data.adjustments && data.adjustments.length > 0) {
                data.adjustments.forEach(adj => {
                    const absVal = Math.abs(adj.adjustment);
                    const sign = adj.adjustment > 0 ? '+' : '-';
                    const badgeClass = adj.adjustment > 0 ? 'positive' : 'negative';
                    
                    const div = document.createElement('div');
                    div.className = 'adjustment-item';
                    div.innerHTML = `
                        <div class="badge ${badgeClass}">${sign}${absVal} ${adj.dimension}</div>
                        <div style="flex:1; font-size:0.9rem; color:var(--text-muted);">${adj.reason}</div>
                    `;
                    adjList.appendChild(div);
                });
                adjContainer.classList.remove('hidden');
            } else {
                adjContainer.classList.add('hidden');
            }

            document.getElementById('scoreResult').classList.remove('hidden');
            
        } catch (err) {
            console.error(err);
        } finally {
            hideLoading();
        }
    });

    // --- 3. Solution Builder ---
    document.getElementById('solutionForm').addEventListener('submit', async (e) => {
        e.preventDefault();
        showLoading();
        
        const payload = {
            idea: document.getElementById('ideaToBuild').value
        };

        try {
            const res = await fetch('/api/build-solution', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(payload)
            });
            const data = await res.json();
            
            let markdownContent = '';
            if(data.tech_stack) {
                markdownContent += `### recommended Tech Stack\n* ${data.tech_stack.join('\n* ')}\n\n`;
                markdownContent += `### Unique Angle / Differentiator\n> ${data.unique_angle}\n\n`;
                markdownContent += `### MVP Execution Roadmap\n`;
                data.mvp_roadmap.forEach((step, i) => {
                    markdownContent += `${i+1}. ${step}\n`;
                });
                
                document.getElementById('solutionResult').innerHTML = marked.parse(markdownContent);
                document.getElementById('solutionResult').classList.remove('hidden');
            }
        } catch (err) {
            console.error(err);
        } finally {
            hideLoading();
        }
    });

    // --- 4. Pitch Generator ---
    document.getElementById('pitchForm').addEventListener('submit', async (e) => {
        e.preventDefault();
        showLoading();
        
        const payload = {
            idea: document.getElementById('ideaToPitch').value
        };

        try {
            const res = await fetch('/api/generate-pitch', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(payload)
            });
            const data = await res.json();
            
            if(data.hook) {
                const markdownContent = `
### 🎣 The Hook (10s)
> *${data.hook}*

### 😡 The Problem (15s)
${data.problem}

### 💡 The Solution (15s)
${data.solution}

### 💻 The Demo / Vision (15s)
${data.demo}

### 🎤 The Ask (5s)
**${data.ask}**
`;
                document.getElementById('pitchResult').innerHTML = marked.parse(markdownContent);
                document.getElementById('pitchResult').classList.remove('hidden');
            }
        } catch (err) {
            console.error(err);
        } finally {
            hideLoading();
        }
    });

});
