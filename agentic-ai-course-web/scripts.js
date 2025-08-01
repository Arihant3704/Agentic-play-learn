document.addEventListener("DOMContentLoaded", () => {
    const sidebar = document.getElementById("sidebar");
    const courseContent = document.getElementById("course-content");
    const loadingIndicator = document.querySelector(".loading-indicator");

    const modules = [
        {
            title: "Module 1: Introduction to Agentic AI",
            lessons: [
                { title: "What is Agentic AI?", path: "../module1_introduction_to_agentic_ai/lessons/01_what_is_agentic_ai.md" },
                { title: "History and Evolution of AI Agents", path: "../module1_introduction_to_agentic_ai/lessons/02_history_and_evolution.md" },
                { title: "Key Components of an AI Agent", path: "../module1_introduction_to_agentic_ai/lessons/03_key_components.md" },
                { title: "Applications of Agentic AI", path: "../module1_introduction_to_agentic_ai/lessons/04_applications_of_agentic_ai.md" },
            ],
            assignment: { title: "Module 1 Quiz", path: "../module1_introduction_to_agentic_ai/assignment/module1_quiz.md" },
        },
        {
            title: "Module 2: Building Your First AI Agent",
            lessons: [
                { title: "Setting up Your Development Environment", path: "../module2_building_your_first_ai_agent/lessons/01_setting_up_the_environment.md" },
                { title: "Introduction to LangChain", path: "../module2_building_your_first_ai_agent/lessons/02_introduction_to_langchain.md" },
                { title: "Creating a Simple AI Agent", path: "../module2_building_your_first_ai_agent/lessons/03_creating_a_simple_agent.md" },
                { title: "Interacting with Your AI Agent", path: "../module2_building_your_first_ai_agent/lessons/04_interacting_with_your_agent.md" },
            ],
            assignment: { title: "Module 2 Assignment", path: "../module2_building_your_first_ai_agent/assignment/module2_assignment.md" },
        },
        {
            title: "Module 3: Advanced Agent Architectures",
            lessons: [
                { title: "Multi-Agent Systems", path: "../module3_advanced_agent_architectures/lessons/01_multi_agent_systems.md" },
                { title: "Memory and Learning in Agents", path: "../module3_advanced_agent_architectures/lessons/02_memory_and_learning.md" },
                { title: "Planning and Task Decomposition", path: "../module3_advanced_agent_architectures/lessons/03_planning_and_task_decomposition.md" },
                { title: "Integrating Tools and APIs", path: "../module3_advanced_agent_architectures/lessons/04_integrating_tools_and_apis.md" },
            ],
            assignment: { title: "Module 3 Assignment", path: "../module3_advanced_agent_architectures/assignment/module3_assignment.md" },
        },
        {
            title: "Module 4: Agentic AI in the Real World",
            lessons: [
                { title: "Case Studies of Agentic AI Applications", path: "../module4_agentic_ai_in_the_real_world/lessons/01_case_studies.md" },
                { title: "Ethical Considerations and Challenges", path: "../module4_agentic_ai_in_the_real_world/lessons/02_ethical_considerations.md" },
                { title: "The Future of Agentic AI", path: "../module4_agentic_ai_in_the_real_world/lessons/03_the_future_of_agentic_ai.md" },
            ],
            assignment: { title: "Module 4 Assignment", path: "../module4_agentic_ai_in_the_real_world/assignment/module4_assignment.md" },
        },
        {
            title: "Module 5: Agentic AI in Smart Mobility",
            lessons: [
                { title: "The Role of Agentic AI in Smart Mobility", path: "../module5_agentic_ai_in_smart_mobility/lessons/01_role_of_agentic_ai.md" },
                { title: "Designing an In-Car Personal Assistant", path: "../module5_agentic_ai_in_smart_mobility/lessons/02_designing_an_in_car_assistant.md" },
                { title: "Prototyping with a Digital Twin", path: "../module5_agentic_ai_in_smart_mobility/lessons/03_prototyping_with_a_digital_twin.md" },
            ],
            assignment: { title: "Module 5 Assignment", path: "../module5_agentic_ai_in_smart_mobility/assignment/module5_assignment.md" },
        },
        {
            title: "Module 6: Agentic AI in UGV",
            lessons: [
                { title: "Introduction to Unmanned Ground Vehicles (UGVs)", path: "../module6_agentic_ai_in_ugv/lessons/01_introduction_to_ugv.md" },
                { title: "Agentic AI for UGV Navigation", path: "../module6_agentic_ai_in_ugv/lessons/02_agentic_ai_for_ugv_navigation.md" },
                { title: "UGV Mission Planning", path: "../module6_agentic_ai_in_ugv/lessons/03_ugv_mission_planning.md" },
            ],
            assignment: { title: "Module 6 Assignment", path: "../module6_agentic_ai_in_ugv/assignment/module6_assignment.md" },
        },
        {
            title: "Module 7: Agentic AI in UAV",
            lessons: [
                { title: "Introduction to Unmanned Aerial Vehicles (UAVs)", path: "../module7_agentic_ai_in_uav/lessons/01_introduction_to_uav.md" },
                { title: "Agentic AI for UAV Flight Control", path: "../module7_agentic_ai_in_uav/lessons/02_agentic_ai_for_uav_flight_control.md" },
                { title: "UAV Swarm Intelligence", path: "../module7_agentic_ai_in_uav/lessons/03_uav_swarm_intelligence.md" },
            ],
            assignment: { title: "Module 7 Assignment", path: "../module7_agentic_ai_in_uav/assignment/module7_assignment.md" },
        },
        {
            title: "Module 8: Project - The AI Co-Pilot",
            lessons: [
                { title: "Understanding the Hackathon", path: "../module8_gemma_3n_hackathon/lessons/01_understanding_the_hackathon.md" },
                { title: "Brainstorming for Automotive Impact", path: "../module8_gemma_3n_hackathon/lessons/02_brainstorming_for_impact.md" },
                { title: "Designing the AI Co-Pilot", path: "../module8_gemma_3n_hackathon/lessons/03_designing_your_solution.md" },
                { title: "Deep Dive Case Study: The AI Co-Pilot Agent", path: "../module8_gemma_3n_hackathon/lessons/04_case_study_kitchen_navigator.md" },
            ],
            assignment: { title: "Module 8 Assignment: AI Co-Pilot Project Proposal", path: "../module8_gemma_3n_hackathon/assignment/module8_assignment.md" },
        },
        {
            title: "Module 9: Human-AI Interaction on the Edge",
            lessons: [
                { title: "The Power of On-Device AI", path: "../module9_human_ai_interaction/lessons/01_on_device_ai.md" },
                { title: "Novel Human-AI Interaction (H-AI)", path: "../module9_human_ai_interaction/lessons/02_novel_human_ai_interaction.md" },
                { title: "Designing an Edge-First, H-AI System", path: "../module9_human_ai_interaction/lessons/03_designing_an_edge_ai_system.md" },
            ],
            assignment: { title: "Module 9 Assignment: Design the Next Generation of H-AI", path: "../module9_human_ai_interaction/assignment/module9_assignment.md" },
        },
        {
            title: "Module 10: The Samsung EnnovateX AI Challenge",
            lessons: [
                { title: "Understanding the Challenge", path: "../module10_samsung_ennovatex/lessons/01_understanding_the_challenge.md" },
                { title: "Analyzing the Problem Statements", path: "../module10_samsung_ennovatex/lessons/02_analyzing_the_problems.md" },
                { title: "Designing the \"Always-On AI Companion\"", path: "../module10_samsung_ennovatex/lessons/03_designing_the_ai_companion.md" },
            ],
            assignment: { title: "Module 10 Assignment: Samsung EnnovateX Project Proposal", path: "../module10_samsung_ennovatex/assignment/module10_assignment.md" },
        },
    ];

    // --- Sidebar Population ---
    const sidebarList = document.createElement("ul");
    modules.forEach((module, moduleIndex) => {
        const moduleItem = document.createElement("li");
        const moduleLink = document.createElement("a");
        moduleLink.textContent = module.title;
        moduleLink.href = "#";
        moduleLink.addEventListener("click", (e) => {
            e.preventDefault();
            // Toggle lesson visibility
            const lessonsList = moduleItem.querySelector("ul");
            lessonsList.style.display = lessonsList.style.display === "none" ? "block" : "none";
        });
        moduleItem.appendChild(moduleLink);

        const lessonsList = document.createElement("ul");
        lessonsList.style.display = "none";

        module.lessons.forEach((lesson, lessonIndex) => {
            const lessonItem = document.createElement("li");
            const lessonLink = document.createElement("a");
            lessonLink.textContent = lesson.title;
            lessonLink.href = "#";
            lessonLink.addEventListener("click", (e) => {
                e.preventDefault();
                loadContent(lesson.path, lessonLink);
            });
            lessonItem.appendChild(lessonLink);
            lessonsList.appendChild(lessonItem);
        });

        if (module.assignment) {
            const assignmentItem = document.createElement("li");
            const assignmentLink = document.createElement("a");
            assignmentLink.textContent = module.assignment.title;
            assignmentLink.href = "#";
            assignmentLink.addEventListener("click", (e) => {
                e.preventDefault();
                loadContent(module.assignment.path, assignmentLink);
            });
            assignmentItem.appendChild(assignmentLink);
            lessonsList.appendChild(assignmentItem);
        }

        moduleItem.appendChild(lessonsList);
        sidebarList.appendChild(moduleItem);
    });
    sidebar.appendChild(sidebarList);

    // --- Content Loading ---
    function loadContent(path, linkElement) {
        loadingIndicator.style.display = "block";
        courseContent.innerHTML = "";

        fetch(path)
            .then(response => response.text())
            .then(text => {
                loadingIndicator.style.display = "none";
                const content = document.createElement("div");
                content.innerHTML = text;
                courseContent.appendChild(content);
                hljs.highlightAll();

                // --- Progress Tracking ---
                if (linkElement) {
                    const allLinks = document.querySelectorAll("#sidebar a");
                    allLinks.forEach(link => link.classList.remove("active"));
                    linkElement.classList.add("active");
                    localStorage.setItem("activeLesson", path);
                }
            });
    }

    // --- Load Last Active Lesson ---
    const activeLesson = localStorage.getItem("activeLesson");
    if (activeLesson) {
        const link = document.querySelector(`[href="#"][data-path="${activeLesson}"]`);
        if (link) {
            loadContent(activeLesson, link);
        }
    }

    // --- Handle Module Selection from Dashboard ---
    const urlParams = new URLSearchParams(window.location.search);
    const moduleNumber = urlParams.get('module');
    if (moduleNumber) {
        const moduleIndex = parseInt(moduleNumber) - 1;
        if (moduleIndex >= 0 && moduleIndex < modules.length) {
            const lessonsList = sidebar.querySelectorAll('ul ul')[moduleIndex];
            lessonsList.style.display = 'block';
            if (lessonsList.children.length > 0) {
                const firstLessonLink = lessonsList.children[0].querySelector('a');
                loadContent(modules[moduleIndex].lessons[0].path, firstLessonLink);
            }
        }
    }
});