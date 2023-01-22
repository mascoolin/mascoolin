describe('positif login & negatif', () => {
  it('passes', () => {
    cy.visit('https://the-internet.herokuapp.com/login')

    cy.get('#username')
    .type('tomsmith')
    .should('be.visible')
    cy.wait(2)

    cy.get('#password')
    .type('SuperSecretPassword!')
    cy.wait(2)
    cy.get('.fa').click()
    cy.wait(5)
  })

  it('passes', () => {
    cy.visit('https://the-internet.herokuapp.com/login')

    cy.get('#username')
    .type('toms')
    .should('be.visible')
    cy.wait(2)

    cy.get('#password')
    .type('Super')
    cy.wait(2)
    cy.get('.fa').click()
    cy.get('#flash')
    .should('be.visible')
  })
})