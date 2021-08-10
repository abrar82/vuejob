<template>
  <div id="app" class="wrapper">
 <!-- <form @submit.prevent="showJobs"> -->
      <input type="text" name="todo-text" v-model="newUser" placeholder="New todo">
    <button type="submit" @click.prevent="showJobs" class="subBtn">Submit</button>
    <!-- <button type="submit"  class="subBtn">Submit</button> -->
    <!-- </form> -->
    <div v-if="isRec">
<h1>Recruiter UI</h1>

<Recruiter></Recruiter>
    </div>
    <div v-else-if="isCand">
<h1>Candidate UI</h1>
<Candidate></Candidate>
    </div>
    <div v-else>

<h1>Welcome</h1>
    </div>
  </div>
</template>

<script>
import Candidate from './views/Candidate.vue'
import Recruiter from './views/Recruiter.vue'
export default{
  components: {
    Candidate,
    Recruiter
  },
  data(){
    return{
      recruiter:"recruiter@screel.in",
      candidate:"candidate@screel.in",
      isRec:false,
      isCand:false,
      newUser:""
    }
  },
    methods: {
    showJobs() {
      const trimmedText = this.newUser.trim()
      if(!trimmedText){
        this.isRec = false
        this.isCand = false
         console.log(trimmedText +" s"+ this.isCand + " "+ this.isRec)
      
      }else{
    if (trimmedText===this.recruiter) {
       
        this.isRec = true
        this.isCand = false
        
       
        console.log(trimmedText +" "+ this.isCand + " "+ this.isRec)
      }else if(trimmedText===this.candidate){
     
        this.isCand = true
        this.isRec = false
       
        console.log(trimmedText +" "+ this.isCand + " "+ this.isRec)
      }

      this.newUser = ""

      }
          },
}
}
</script>


<style >

</style>
