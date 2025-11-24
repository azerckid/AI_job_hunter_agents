# Interview Preparation Guide: Senior Fullstack Engineer at Mangomint

## Company Overview

| Attribute | Detail |
| :--- | :--- |
| **Company Name** | Mangomint |
| **Industry** | Beauty, Wellness, SaaS (Salon/Spa Management Software) |
| **Size** | 51-200 employees (Scale-up/Growth Stage) |
| **Core Product** | Modern, intuitive cloud-based software providing booking, POS, client management, and business tools for high-end salons and spas. |
| **Hiring Context** | The role focuses on an ambitious, experimental *new* product line: **SalonJobs**. This suggests Mangomint is aggressively expanding its platform ecosystem beyond core management to capture the talent market within the industry. |
| **Culture Signal** | High emphasis on design, modern technology (Next.js/TypeScript), remote-first execution, and speed/iteration (startup within a larger entity). |

## Mission and Values

Mangomint’s core mission revolves around providing high-quality, modern business tools to the beauty and wellness industry, which traditionally uses fragmented or outdated software.

**Inferred Values based on Job Description and Industry Position:**

*   **Entrepreneurial Ownership:** Explicitly required—comfort with ambiguity, owning outcomes, and taking initiative on major technical decisions. This role is about building, not just maintaining.
*   **Design and Product Quality:** A key differentiator for Mangomint is providing a clean, polished user experience. Engineers must possess a "strong product sense" and collaborate closely with designers (Figma to product).
*   **Fast Iteration & Learning:** Emphasis on working in "short, focused cycles that prioritize learning and experimentation." Speed to market and willingness to pivot are crucial for the experimental SalonJobs project.
*   **Architectural Stewardship:** Senior engineers are expected to define and own the architecture (frameworks, infrastructure), ensuring scalability and maintainability for this new venture.

## Recent News or Changes

The most relevant news for this role is the internal investment in, and focus on, **SalonJobs**.

*   **Product Expansion:** Mangomint is moving beyond its core SaaS offering (scheduling, payments) into the talent acquisition and job market space. This indicates a high-growth strategy aimed at cementing itself as the "de facto" platform for the entire industry lifecycle.
*   **Strategic Investment in Green Field Projects:** SalonJobs is described as "experimental and ambitious." This project likely has high visibility within the company and requires engineers who thrive on high impact and risk.
*   **Modernization of Stack:** The technology list (`Next.js`, `Drizzle ORM`, `Vercel`, `Supabase`) suggests a commitment to using the latest, most efficient tools, optimizing for development speed and developer experience, which is common when spinning up high-velocity new products.

## Role Context and Product Involvement

The **Senior Fullstack Engineer** is not a team member on the core Mangomint platform but a technical leader for the **SalonJobs** initiative.

*   **Team Structure & Authority:** This is a small, highly motivated team, implying the candidate will be one of the foundational technical leaders, or potentially *the* technical leader, for this specific product line. The role demands significant autonomy.
*   **Product Context (SalonJobs):** This product aims to solve the hiring crisis/job search inefficiencies in the beauty and wellness sector. The engineer must build features that achieve Product Market Fit (PMF) quickly.
*   **Technical Mandate:** The candidate must "Own major technical decisions across the stack." This includes architecture, choice of tooling (within the prescribed stack), and infrastructure setup. Success hinges on rapid development combined with sound, scalable architectural choices for the future.
*   **Product Focus:** The role requires strong collaboration with Product and Design, suggesting the engineer will be heavily involved in refining requirements and user experience, not just executing tickets.

## Likely Interview Topics

Candidates should prepare to discuss specific past examples related to *architectural ownership* and *speed/ambiguity* using the modern tech stack.

### 1. Architectural and Technical Deep Dive

*   **Next.js Scaling and Decisions:**
    *   *Question:* Describe a recent complex application you built with Next.js. How did you decide between Server Components vs. Client Components, and how did you manage data fetching and caching using tools like Vercel/Supabase?
    *   *Focus:* Demonstrate expertise in modern React/Next.js paradigms, especially performance and deployment architecture.
*   **Backend Strategy & ORMs (Node/Drizzle/PostgreSQL):**
    *   *Question:* Walk us through a decision process where you migrated or chose a specific ORM (like Drizzle) for a project. What were the trade-offs regarding type safety, performance, and developer experience compared to alternatives (e.g., Prisma)?
    *   *Focus:* Expertise in the specific stack and justification for architectural choices.
*   **Infrastructure & DevOps:**
    *   *Question:* Since you will own infrastructure decisions (Vercel, Docker, Sentry), describe how you set up CI/CD and monitoring for a high-velocity, experimental product to ensure rapid releases don't compromise stability.

### 2. Entrepreneurial Mindset and Ownership

*   **Dealing with Ambiguity and PMF:**
    *   *Question:* Tell us about a project where the requirements were vague or changed constantly because you were searching for Product Market Fit. How did you structure the engineering work to maximize learning in "short, focused cycles"?
    *   *Focus:* Demonstrate comfort with iterative development and prioritizing outcomes over rigid plans.
*   **Technical Leadership and Buy-in:**
    *   *Question:* You are tasked with selecting a new foundational technology for SalonJobs. How do you propose, gain alignment, and then successfully implement a significant architectural change while remaining a hands-on contributor?
    *   *Focus:* Leadership skills, communication, and the ability to balance strategic thinking with execution.

### 3. Product Sense and Design Collaboration

*   **Design to Production Workflow:**
    *   *Question:* Describe a project where you collaborated directly with a designer (e.g., using Figma). How did you balance rapid implementation deadlines with ensuring the final product delivered a polished, high-quality user experience?
    *   *Focus:* Ability to translate design concepts faithfully and contribute to UX discussions, essential for a B2B SaaS platform that values design.

## Suggested Questions to Ask

These questions are designed to show the candidate understands the critical nature of the **SalonJobs** project and the responsibilities of architectural leadership.

### Regarding the SalonJobs Product

1.  "Since SalonJobs is described as an experimental and ambitious venture, what are the **key metrics or hypotheses** the team is currently prioritizing to prove product-market fit (PMF) over the next 6-12 months?"
2.  "What is the intended architectural relationship between SalonJobs and the existing core Mangomint platform? Will we be integrating authentication, data, or shared microservices, and how will that technical strategy evolve?"
3.  "How does the engineering team currently prioritize technical debt vs. fast iteration/feature delivery on a new project like this?"

### Regarding the Role and Team

4.  "Given the requirement to 'own major technical decisions,' how does Mangomint balance decentralized ownership within a small team against ensuring long-term technical cohesion across the broader engineering organization?"
5.  "Can you describe the composition of the immediate SalonJobs team (Product Manager, Designer, other engineers) and what the typical cadence is for those short, focused learning cycles?"
6.  "What does success look like for the Senior Fullstack Engineer in this role *beyond* shipping code—specifically regarding mentoring, architectural stability, or setting team standards?"